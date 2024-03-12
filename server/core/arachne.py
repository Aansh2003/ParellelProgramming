# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _arachne_nn
else:
    import _arachne_nn

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class SwigPyIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _arachne_nn.delete_SwigPyIterator

    def value(self):
        return _arachne_nn.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _arachne_nn.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _arachne_nn.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _arachne_nn.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _arachne_nn.SwigPyIterator_equal(self, x)

    def copy(self):
        return _arachne_nn.SwigPyIterator_copy(self)

    def next(self):
        return _arachne_nn.SwigPyIterator_next(self)

    def __next__(self):
        return _arachne_nn.SwigPyIterator___next__(self)

    def previous(self):
        return _arachne_nn.SwigPyIterator_previous(self)

    def advance(self, n):
        return _arachne_nn.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _arachne_nn.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _arachne_nn.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _arachne_nn.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _arachne_nn.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _arachne_nn.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _arachne_nn.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _arachne_nn:
_arachne_nn.SwigPyIterator_swigregister(SwigPyIterator)

class IntVector(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _arachne_nn.IntVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _arachne_nn.IntVector___nonzero__(self)

    def __bool__(self):
        return _arachne_nn.IntVector___bool__(self)

    def __len__(self):
        return _arachne_nn.IntVector___len__(self)

    def __getslice__(self, i, j):
        return _arachne_nn.IntVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _arachne_nn.IntVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _arachne_nn.IntVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _arachne_nn.IntVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _arachne_nn.IntVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _arachne_nn.IntVector___setitem__(self, *args)

    def pop(self):
        return _arachne_nn.IntVector_pop(self)

    def append(self, x):
        return _arachne_nn.IntVector_append(self, x)

    def empty(self):
        return _arachne_nn.IntVector_empty(self)

    def size(self):
        return _arachne_nn.IntVector_size(self)

    def swap(self, v):
        return _arachne_nn.IntVector_swap(self, v)

    def begin(self):
        return _arachne_nn.IntVector_begin(self)

    def end(self):
        return _arachne_nn.IntVector_end(self)

    def rbegin(self):
        return _arachne_nn.IntVector_rbegin(self)

    def rend(self):
        return _arachne_nn.IntVector_rend(self)

    def clear(self):
        return _arachne_nn.IntVector_clear(self)

    def get_allocator(self):
        return _arachne_nn.IntVector_get_allocator(self)

    def pop_back(self):
        return _arachne_nn.IntVector_pop_back(self)

    def erase(self, *args):
        return _arachne_nn.IntVector_erase(self, *args)

    def __init__(self, *args):
        _arachne_nn.IntVector_swiginit(self, _arachne_nn.new_IntVector(*args))

    def push_back(self, x):
        return _arachne_nn.IntVector_push_back(self, x)

    def front(self):
        return _arachne_nn.IntVector_front(self)

    def back(self):
        return _arachne_nn.IntVector_back(self)

    def assign(self, n, x):
        return _arachne_nn.IntVector_assign(self, n, x)

    def resize(self, *args):
        return _arachne_nn.IntVector_resize(self, *args)

    def insert(self, *args):
        return _arachne_nn.IntVector_insert(self, *args)

    def reserve(self, n):
        return _arachne_nn.IntVector_reserve(self, n)

    def capacity(self):
        return _arachne_nn.IntVector_capacity(self)
    __swig_destroy__ = _arachne_nn.delete_IntVector

# Register IntVector in _arachne_nn:
_arachne_nn.IntVector_swigregister(IntVector)

class FloatTensorVector(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _arachne_nn.FloatTensorVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _arachne_nn.FloatTensorVector___nonzero__(self)

    def __bool__(self):
        return _arachne_nn.FloatTensorVector___bool__(self)

    def __len__(self):
        return _arachne_nn.FloatTensorVector___len__(self)

    def __getslice__(self, i, j):
        return _arachne_nn.FloatTensorVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _arachne_nn.FloatTensorVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _arachne_nn.FloatTensorVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _arachne_nn.FloatTensorVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _arachne_nn.FloatTensorVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _arachne_nn.FloatTensorVector___setitem__(self, *args)

    def pop(self):
        return _arachne_nn.FloatTensorVector_pop(self)

    def append(self, x):
        return _arachne_nn.FloatTensorVector_append(self, x)

    def empty(self):
        return _arachne_nn.FloatTensorVector_empty(self)

    def size(self):
        return _arachne_nn.FloatTensorVector_size(self)

    def swap(self, v):
        return _arachne_nn.FloatTensorVector_swap(self, v)

    def begin(self):
        return _arachne_nn.FloatTensorVector_begin(self)

    def end(self):
        return _arachne_nn.FloatTensorVector_end(self)

    def rbegin(self):
        return _arachne_nn.FloatTensorVector_rbegin(self)

    def rend(self):
        return _arachne_nn.FloatTensorVector_rend(self)

    def clear(self):
        return _arachne_nn.FloatTensorVector_clear(self)

    def get_allocator(self):
        return _arachne_nn.FloatTensorVector_get_allocator(self)

    def pop_back(self):
        return _arachne_nn.FloatTensorVector_pop_back(self)

    def erase(self, *args):
        return _arachne_nn.FloatTensorVector_erase(self, *args)

    def __init__(self, *args):
        _arachne_nn.FloatTensorVector_swiginit(self, _arachne_nn.new_FloatTensorVector(*args))

    def push_back(self, x):
        return _arachne_nn.FloatTensorVector_push_back(self, x)

    def front(self):
        return _arachne_nn.FloatTensorVector_front(self)

    def back(self):
        return _arachne_nn.FloatTensorVector_back(self)

    def assign(self, n, x):
        return _arachne_nn.FloatTensorVector_assign(self, n, x)

    def resize(self, *args):
        return _arachne_nn.FloatTensorVector_resize(self, *args)

    def insert(self, *args):
        return _arachne_nn.FloatTensorVector_insert(self, *args)

    def reserve(self, n):
        return _arachne_nn.FloatTensorVector_reserve(self, n)

    def capacity(self):
        return _arachne_nn.FloatTensorVector_capacity(self)

# Register FloatTensorVector in _arachne_nn:
_arachne_nn.FloatTensorVector_swigregister(FloatTensorVector)

class FloatTensor(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _arachne_nn.FloatTensor_swiginit(self, _arachne_nn.new_FloatTensor(*args))

    @staticmethod
    def readCSV(filename):
        return _arachne_nn.FloatTensor_readCSV(filename)

    def Normalize(self):
        return _arachne_nn.FloatTensor_Normalize(self)

    def multiply(self, arg2):
        return _arachne_nn.FloatTensor_multiply(self, arg2)

    def OMPmultiply(self, arg2):
        return _arachne_nn.FloatTensor_OMPmultiply(self, arg2)

    def elem_multiply(self, arg2):
        return _arachne_nn.FloatTensor_elem_multiply(self, arg2)

    def scalarMultiply(self, arg2):
        return _arachne_nn.FloatTensor_scalarMultiply(self, arg2)

    def OMPscalarMultiply(self, arg2):
        return _arachne_nn.FloatTensor_OMPscalarMultiply(self, arg2)

    def add(self, arg2):
        return _arachne_nn.FloatTensor_add(self, arg2)

    def OMPadd(self, arg2):
        return _arachne_nn.FloatTensor_OMPadd(self, arg2)

    def scalarAdd(self, arg2):
        return _arachne_nn.FloatTensor_scalarAdd(self, arg2)

    def divide(self, arg2):
        return _arachne_nn.FloatTensor_divide(self, arg2)

    def convertFloat(self):
        return _arachne_nn.FloatTensor_convertFloat(self)

    def flatten(self):
        return _arachne_nn.FloatTensor_flatten(self)

    def reshape(self, arg2):
        return _arachne_nn.FloatTensor_reshape(self, arg2)

    def sqrt(self):
        return _arachne_nn.FloatTensor_sqrt(self)

    @staticmethod
    def randomTensor(*args):
        return _arachne_nn.FloatTensor_randomTensor(*args)

    @staticmethod
    def randomFloatTensor(arg1):
        return _arachne_nn.FloatTensor_randomFloatTensor(arg1)

    def row_split(self):
        return _arachne_nn.FloatTensor_row_split(self)

    def input_output_split(self, arg2):
        return _arachne_nn.FloatTensor_input_output_split(self, arg2)
    __swig_destroy__ = _arachne_nn.delete_FloatTensor

    def max(self):
        return _arachne_nn.FloatTensor_max(self)

    def argmax(self):
        return _arachne_nn.FloatTensor_argmax(self)

    def min(self):
        return _arachne_nn.FloatTensor_min(self)

    def argmin(self):
        return _arachne_nn.FloatTensor_argmin(self)

    def transpose(self):
        return _arachne_nn.FloatTensor_transpose(self)

    def OMPtranspose(self):
        return _arachne_nn.FloatTensor_OMPtranspose(self)

    def map(self, func):
        return _arachne_nn.FloatTensor_map(self, func)

    def copy(self):
        return _arachne_nn.FloatTensor_copy(self)

    def __add__(self, other):
        return _arachne_nn.FloatTensor___add__(self, other)

    def __sub__(self, other):
        return _arachne_nn.FloatTensor___sub__(self, other)

    def __mul__(self, other):
        return _arachne_nn.FloatTensor___mul__(self, other)

    def getSize(self):
        return _arachne_nn.FloatTensor_getSize(self)

    def printSize(self):
        return _arachne_nn.FloatTensor_printSize(self)

    def printTensor(self):
        return _arachne_nn.FloatTensor_printTensor(self)
    data = property(_arachne_nn.FloatTensor_data_get, _arachne_nn.FloatTensor_data_set)
    size = property(_arachne_nn.FloatTensor_size_get, _arachne_nn.FloatTensor_size_set)

# Register FloatTensor in _arachne_nn:
_arachne_nn.FloatTensor_swigregister(FloatTensor)

def FloatTensor_readCSV(filename):
    return _arachne_nn.FloatTensor_readCSV(filename)

def FloatTensor_randomTensor(*args):
    return _arachne_nn.FloatTensor_randomTensor(*args)

def FloatTensor_randomFloatTensor(arg1):
    return _arachne_nn.FloatTensor_randomFloatTensor(arg1)

class FloatTensorPair(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _arachne_nn.FloatTensorPair_swiginit(self, _arachne_nn.new_FloatTensorPair(*args))
    first = property(_arachne_nn.FloatTensorPair_first_get, _arachne_nn.FloatTensorPair_first_set)
    second = property(_arachne_nn.FloatTensorPair_second_get, _arachne_nn.FloatTensorPair_second_set)
    def __len__(self):
        return 2
    def __repr__(self):
        return str((self.first, self.second))
    def __getitem__(self, index): 
        if not (index % 2):
            return self.first
        else:
            return self.second
    def __setitem__(self, index, val):
        if not (index % 2):
            self.first = val
        else:
            self.second = val
    __swig_destroy__ = _arachne_nn.delete_FloatTensorPair

# Register FloatTensorPair in _arachne_nn:
_arachne_nn.FloatTensorPair_swigregister(FloatTensorPair)

class IntPair(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _arachne_nn.IntPair_swiginit(self, _arachne_nn.new_IntPair(*args))
    first = property(_arachne_nn.IntPair_first_get, _arachne_nn.IntPair_first_set)
    second = property(_arachne_nn.IntPair_second_get, _arachne_nn.IntPair_second_set)
    def __len__(self):
        return 2
    def __repr__(self):
        return str((self.first, self.second))
    def __getitem__(self, index): 
        if not (index % 2):
            return self.first
        else:
            return self.second
    def __setitem__(self, index, val):
        if not (index % 2):
            self.first = val
        else:
            self.second = val
    __swig_destroy__ = _arachne_nn.delete_IntPair

# Register IntPair in _arachne_nn:
_arachne_nn.IntPair_swigregister(IntPair)

class Model(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def forward(self, arg2):
        return _arachne_nn.Model_forward(self, arg2)

    def OMPforward(self, arg2):
        return _arachne_nn.Model_OMPforward(self, arg2)

    def backward(self, arg2, arg3, arg4):
        return _arachne_nn.Model_backward(self, arg2, arg3, arg4)

    def OMPbackward(self, arg2, arg3):
        return _arachne_nn.Model_OMPbackward(self, arg2, arg3)

    def computeGradients(self, arg2, arg3, arg4):
        return _arachne_nn.Model_computeGradients(self, arg2, arg3, arg4)

    def OMPcomputeGradients(self, arg2, arg3):
        return _arachne_nn.Model_OMPcomputeGradients(self, arg2, arg3)

    def getGradients(self):
        return _arachne_nn.Model_getGradients(self)
    __swig_destroy__ = _arachne_nn.delete_Model

    def getParamCount(self):
        return _arachne_nn.Model_getParamCount(self)

    def getInputSize(self):
        return _arachne_nn.Model_getInputSize(self)

    def getOutputSize(self):
        return _arachne_nn.Model_getOutputSize(self)
    trainable = property(_arachne_nn.Model_trainable_get, _arachne_nn.Model_trainable_set)
    type = property(_arachne_nn.Model_type_get, _arachne_nn.Model_type_set)
    isforward = property(_arachne_nn.Model_isforward_get, _arachne_nn.Model_isforward_set)
    weights = property(_arachne_nn.Model_weights_get, _arachne_nn.Model_weights_set)
    gradients = property(_arachne_nn.Model_gradients_get, _arachne_nn.Model_gradients_set)
    inputs = property(_arachne_nn.Model_inputs_get, _arachne_nn.Model_inputs_set)

# Register Model in _arachne_nn:
_arachne_nn.Model_swigregister(Model)

class Activation(Model):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def forward(self, arg2):
        return _arachne_nn.Activation_forward(self, arg2)

    def OMPforward(self, arg2):
        return _arachne_nn.Activation_OMPforward(self, arg2)

    def getParamCount(self):
        return _arachne_nn.Activation_getParamCount(self)

    def getInputSize(self):
        return _arachne_nn.Activation_getInputSize(self)

    def getOutputSize(self):
        return _arachne_nn.Activation_getOutputSize(self)
    inputSize = property(_arachne_nn.Activation_inputSize_get, _arachne_nn.Activation_inputSize_set)
    __swig_destroy__ = _arachne_nn.delete_Activation

# Register Activation in _arachne_nn:
_arachne_nn.Activation_swigregister(Activation)

class Normalize(Model):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, inputSize):
        _arachne_nn.Normalize_swiginit(self, _arachne_nn.new_Normalize(inputSize))

    def getParamCount(self):
        return _arachne_nn.Normalize_getParamCount(self)

    def getInputSize(self):
        return _arachne_nn.Normalize_getInputSize(self)

    def getOutputSize(self):
        return _arachne_nn.Normalize_getOutputSize(self)

    def forward(self, arg2):
        return _arachne_nn.Normalize_forward(self, arg2)

    def OMPforward(self, arg2):
        return _arachne_nn.Normalize_OMPforward(self, arg2)
    __swig_destroy__ = _arachne_nn.delete_Normalize

# Register Normalize in _arachne_nn:
_arachne_nn.Normalize_swigregister(Normalize)

class Optimizer(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def update_weights(self, arg2, arg3, arg4):
        return _arachne_nn.Optimizer_update_weights(self, arg2, arg3, arg4)
    __swig_destroy__ = _arachne_nn.delete_Optimizer

# Register Optimizer in _arachne_nn:
_arachne_nn.Optimizer_swigregister(Optimizer)

class Adam(Optimizer):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, lr=0.001, beta1=0.9, beta2=0.999, epsilon=1e-7):
        _arachne_nn.Adam_swiginit(self, _arachne_nn.new_Adam(lr, beta1, beta2, epsilon))

    def update_weights(self, arg2, arg3, arg4):
        return _arachne_nn.Adam_update_weights(self, arg2, arg3, arg4)
    __swig_destroy__ = _arachne_nn.delete_Adam

# Register Adam in _arachne_nn:
_arachne_nn.Adam_swigregister(Adam)

class Loss(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def loss(self, arg2, arg3):
        return _arachne_nn.Loss_loss(self, arg2, arg3)

    def derivative(self, arg2, arg3):
        return _arachne_nn.Loss_derivative(self, arg2, arg3)
    __swig_destroy__ = _arachne_nn.delete_Loss

# Register Loss in _arachne_nn:
_arachne_nn.Loss_swigregister(Loss)

class CrossEntropyLoss(Loss):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def loss(self, prediction, actual):
        return _arachne_nn.CrossEntropyLoss_loss(self, prediction, actual)

    def derivative(self, prediction, actual):
        return _arachne_nn.CrossEntropyLoss_derivative(self, prediction, actual)

    def __init__(self):
        _arachne_nn.CrossEntropyLoss_swiginit(self, _arachne_nn.new_CrossEntropyLoss())
    __swig_destroy__ = _arachne_nn.delete_CrossEntropyLoss

# Register CrossEntropyLoss in _arachne_nn:
_arachne_nn.CrossEntropyLoss_swigregister(CrossEntropyLoss)

class Pipeline(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        _arachne_nn.Pipeline_swiginit(self, _arachne_nn.new_Pipeline())
    __swig_destroy__ = _arachne_nn.delete_Pipeline

    def add(self, arg2):
        return _arachne_nn.Pipeline_add(self, arg2)

    def printPipeline(self):
        return _arachne_nn.Pipeline_printPipeline(self)

    def backward(self, arg2, arg3, arg4):
        return _arachne_nn.Pipeline_backward(self, arg2, arg3, arg4)

    def OMPbackward(self, arg2, arg3, arg4):
        return _arachne_nn.Pipeline_OMPbackward(self, arg2, arg3, arg4)

    def forwardFloat(self, input):
        return _arachne_nn.Pipeline_forwardFloat(self, input)

# Register Pipeline in _arachne_nn:
_arachne_nn.Pipeline_swigregister(Pipeline)

class Flatten(Model):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, inputSize):
        _arachne_nn.Flatten_swiginit(self, _arachne_nn.new_Flatten(inputSize))

    def getParamCount(self):
        return _arachne_nn.Flatten_getParamCount(self)

    def getInputSize(self):
        return _arachne_nn.Flatten_getInputSize(self)

    def getOutputSize(self):
        return _arachne_nn.Flatten_getOutputSize(self)

    def forward(self, arg2):
        return _arachne_nn.Flatten_forward(self, arg2)

    def OMPforward(self, arg2):
        return _arachne_nn.Flatten_OMPforward(self, arg2)
    __swig_destroy__ = _arachne_nn.delete_Flatten

# Register Flatten in _arachne_nn:
_arachne_nn.Flatten_swigregister(Flatten)

class Relu(Activation):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _arachne_nn.Relu_swiginit(self, _arachne_nn.new_Relu(*args))

    def forward(self, arg2):
        return _arachne_nn.Relu_forward(self, arg2)

    def OMPforward(self, arg2):
        return _arachne_nn.Relu_OMPforward(self, arg2)
    type = property(_arachne_nn.Relu_type_get, _arachne_nn.Relu_type_set)
    __swig_destroy__ = _arachne_nn.delete_Relu

# Register Relu in _arachne_nn:
_arachne_nn.Relu_swigregister(Relu)

class RMSProp(Optimizer):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, lr=0.001, decay_rate=0.9, epsilon=1e-7):
        _arachne_nn.RMSProp_swiginit(self, _arachne_nn.new_RMSProp(lr, decay_rate, epsilon))

    def update_weights(self, weights, gradient, count):
        return _arachne_nn.RMSProp_update_weights(self, weights, gradient, count)
    __swig_destroy__ = _arachne_nn.delete_RMSProp

# Register RMSProp in _arachne_nn:
_arachne_nn.RMSProp_swigregister(RMSProp)

class Linear(Model):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, inputSize, outputSize):
        _arachne_nn.Linear_swiginit(self, _arachne_nn.new_Linear(inputSize, outputSize))

    def getParamCount(self):
        return _arachne_nn.Linear_getParamCount(self)

    def getInputSize(self):
        return _arachne_nn.Linear_getInputSize(self)

    def getOutputSize(self):
        return _arachne_nn.Linear_getOutputSize(self)

    def forward(self, arg2):
        return _arachne_nn.Linear_forward(self, arg2)

    def OMPforward(self, arg2):
        return _arachne_nn.Linear_OMPforward(self, arg2)

    def printWeights(self):
        return _arachne_nn.Linear_printWeights(self)
    __swig_destroy__ = _arachne_nn.delete_Linear

# Register Linear in _arachne_nn:
_arachne_nn.Linear_swigregister(Linear)

class SGD(Optimizer):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, arg2=1e-2, arg3=0):
        _arachne_nn.SGD_swiginit(self, _arachne_nn.new_SGD(arg2, arg3))

    def update_weights(self, arg2, arg3, arg4):
        return _arachne_nn.SGD_update_weights(self, arg2, arg3, arg4)
    __swig_destroy__ = _arachne_nn.delete_SGD

# Register SGD in _arachne_nn:
_arachne_nn.SGD_swigregister(SGD)

class Softmax(Activation):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _arachne_nn.Softmax_swiginit(self, _arachne_nn.new_Softmax(*args))

    def forward(self, arg2):
        return _arachne_nn.Softmax_forward(self, arg2)

    def OMPforward(self, arg2):
        return _arachne_nn.Softmax_OMPforward(self, arg2)
    type = property(_arachne_nn.Softmax_type_get, _arachne_nn.Softmax_type_set)
    __swig_destroy__ = _arachne_nn.delete_Softmax

# Register Softmax in _arachne_nn:
_arachne_nn.Softmax_swigregister(Softmax)
cvar = _arachne_nn.cvar

class MAELoss(Loss):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def loss(self, arg2, arg3):
        return _arachne_nn.MAELoss_loss(self, arg2, arg3)

    def derivative(self, arg2, arg3):
        return _arachne_nn.MAELoss_derivative(self, arg2, arg3)

    def __init__(self):
        _arachne_nn.MAELoss_swiginit(self, _arachne_nn.new_MAELoss())
    __swig_destroy__ = _arachne_nn.delete_MAELoss

# Register MAELoss in _arachne_nn:
_arachne_nn.MAELoss_swigregister(MAELoss)

class MSELoss(Loss):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def loss(self, arg2, arg3):
        return _arachne_nn.MSELoss_loss(self, arg2, arg3)

    def derivative(self, arg2, arg3):
        return _arachne_nn.MSELoss_derivative(self, arg2, arg3)

    def __init__(self):
        _arachne_nn.MSELoss_swiginit(self, _arachne_nn.new_MSELoss())
    __swig_destroy__ = _arachne_nn.delete_MSELoss

# Register MSELoss in _arachne_nn:
_arachne_nn.MSELoss_swigregister(MSELoss)


