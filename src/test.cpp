#include <iostream>
#include "Tensor.hpp"
#include <utility>
#include <cstdlib>
#include "Linear.hpp"
#include "Flatten.hpp"
#include "Pipeline.hpp"
#include "Relu.hpp"
#include "Normalize.hpp"
#include "MSELoss.hpp"
#include "Adam.hpp"
#include <chrono>
#include "SGD.hpp"
#include "Softmax.hpp"
#include "RMSProp.hpp"
#include "MAELoss.hpp"
#include "CrossEntropyLoss.hpp"
using namespace std;

int main()
{
    pair<int,int> size(4,2);

    Tensor<int> a = Tensor<int>::randomTensor(size);
    
    float **data = new float*[4];
    for(int i=0;i<2;i++)
    {
        data[i] = new float[2];
        for(int j=0;j<4;j++)
        {
            data[i][j] = 1;
        }
    }

    pair<int,int> out_size(4,2);
    Tensor<float> actual = Tensor(data,out_size);
    // actual.flatten().print();
    Tensor<float> dat = Tensor<float>::readCSV("WineQT.csv");
    dat.Normalize().print();
    // a.print();
    // Tensor b = a.copy();
    // b.print();
    // b.print();
    // cout<<"\n";
    // a.OMPtranspose();
    // a.print();
    // cout<<endl;
    // // // b.printSize();
    Pipeline myPipeline;
    Normalize *l = new Normalize(make_pair(4,2));
    Linear* q = new Linear(make_pair(4,2),3);
    Relu* r = new Relu(make_pair(4,3));
    Linear* d = new Linear(make_pair(4,3),2);
    Relu *e = new Relu(make_pair(4,2));

    MSELoss loss_fn;
    // // //Flatten* q = new Flatten(make_pair(4,2));
    // // // q->printWeights();
    myPipeline.add(l);
    myPipeline.add(q);
    myPipeline.add(r);
    myPipeline.add(d);
    myPipeline.add(e);
    myPipeline.printPipeline();
    SGD  optimizer;

    auto start = chrono::high_resolution_clock::now();

    for(int i=0;i<10;i++)
    {
        // a.printSize();
        Tensor<float> out = myPipeline.forward(a);
        // out.printSize();
        // out.print();
        cout<<"Loss at epoch "<<i<<": "<<loss_fn.loss(out,actual)<<endl;

        myPipeline.backward(&optimizer,&loss_fn,actual);
    }
    auto stop = chrono::high_resolution_clock::now();
    auto duration = chrono::duration_cast<chrono::microseconds>(stop - start);
    cout << "\nTime taken for 1000 epochs : "<< duration.count()/1000 << " milliseconds\n";
}
