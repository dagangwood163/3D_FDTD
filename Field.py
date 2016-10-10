# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.10
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_Field')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_Field')
    _Field = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_Field', [dirname(__file__)])
        except ImportError:
            import _Field
            return _Field
        if fp is not None:
            try:
                _mod = imp.load_module('_Field', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _Field = swig_import_helper()
    del swig_import_helper
else:
    import _Field
del _swig_python_version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

class Field(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Field, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Field, name)
    __repr__ = _swig_repr

    def update(self, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18, arg19, arg20, arg21, arg22, arg23, arg24, arg25, arg26, arg27, arg28):
        return _Field.Field_update(self, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18, arg19, arg20, arg21, arg22, arg23, arg24, arg25, arg26, arg27, arg28)

    def setOutputBuffer(self, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
        return _Field.Field_setOutputBuffer(self, arg2, arg3, arg4, arg5, arg6, arg7, arg8)

    def addWaveguideSourceXY(self, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12):
        return _Field.Field_addWaveguideSourceXY(self, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12)

    def a(self, arg2, arg3, arg4):
        return _Field.Field_a(self, arg2, arg3, arg4)

    def update_cpp(self, sampleDistance, nmax, dt, Ex, Ey, Ez, Hx, Hy, Hz, CExdy, CExdz, CEydx, CEydz, CEzdx, CEzdy, CHxdy, CHxdz, CHydx, CHydz, CHzdx, CHzdy, CEx, CEy, CEz):
        return _Field.Field_update_cpp(self, sampleDistance, nmax, dt, Ex, Ey, Ez, Hx, Hy, Hz, CExdy, CExdz, CEydx, CEydz, CEzdx, CEzdy, CHxdy, CHxdz, CHydx, CHydz, CHzdx, CHzdy, CEx, CEy, CEz)

    def setOutputBuffer_cpp(self, OBEx, OBEy, OBEz, OBHx, OBHy, OBHz):
        return _Field.Field_setOutputBuffer_cpp(self, OBEx, OBEy, OBEz, OBHx, OBHy, OBHz)

    def addWaveguideSourceXY_cpp(self, imin, imax, jmin, jmax, k, WGModE, WGModH, WGEx, WGEy, WGHx, WGHy):
        return _Field.Field_addWaveguideSourceXY_cpp(self, imin, imax, jmin, jmax, k, WGModE, WGModH, WGEx, WGEy, WGHx, WGHy)

    def __init__(self):
        this = _Field.new_Field()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _Field.delete_Field
    __del__ = lambda self: None
Field_swigregister = _Field.Field_swigregister
Field_swigregister(Field)

class WaveguideSourceXY(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, WaveguideSourceXY, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, WaveguideSourceXY, name)
    __repr__ = _swig_repr
    __swig_setmethods__["imin"] = _Field.WaveguideSourceXY_imin_set
    __swig_getmethods__["imin"] = _Field.WaveguideSourceXY_imin_get
    if _newclass:
        imin = _swig_property(_Field.WaveguideSourceXY_imin_get, _Field.WaveguideSourceXY_imin_set)
    __swig_setmethods__["imax"] = _Field.WaveguideSourceXY_imax_set
    __swig_getmethods__["imax"] = _Field.WaveguideSourceXY_imax_get
    if _newclass:
        imax = _swig_property(_Field.WaveguideSourceXY_imax_get, _Field.WaveguideSourceXY_imax_set)
    __swig_setmethods__["jmin"] = _Field.WaveguideSourceXY_jmin_set
    __swig_getmethods__["jmin"] = _Field.WaveguideSourceXY_jmin_get
    if _newclass:
        jmin = _swig_property(_Field.WaveguideSourceXY_jmin_get, _Field.WaveguideSourceXY_jmin_set)
    __swig_setmethods__["jmax"] = _Field.WaveguideSourceXY_jmax_set
    __swig_getmethods__["jmax"] = _Field.WaveguideSourceXY_jmax_get
    if _newclass:
        jmax = _swig_property(_Field.WaveguideSourceXY_jmax_get, _Field.WaveguideSourceXY_jmax_set)
    __swig_setmethods__["k"] = _Field.WaveguideSourceXY_k_set
    __swig_getmethods__["k"] = _Field.WaveguideSourceXY_k_get
    if _newclass:
        k = _swig_property(_Field.WaveguideSourceXY_k_get, _Field.WaveguideSourceXY_k_set)
    __swig_setmethods__["sizeY0"] = _Field.WaveguideSourceXY_sizeY0_set
    __swig_getmethods__["sizeY0"] = _Field.WaveguideSourceXY_sizeY0_get
    if _newclass:
        sizeY0 = _swig_property(_Field.WaveguideSourceXY_sizeY0_get, _Field.WaveguideSourceXY_sizeY0_set)
    __swig_setmethods__["sizeY1"] = _Field.WaveguideSourceXY_sizeY1_set
    __swig_getmethods__["sizeY1"] = _Field.WaveguideSourceXY_sizeY1_get
    if _newclass:
        sizeY1 = _swig_property(_Field.WaveguideSourceXY_sizeY1_get, _Field.WaveguideSourceXY_sizeY1_set)
    __swig_setmethods__["modE"] = _Field.WaveguideSourceXY_modE_set
    __swig_getmethods__["modE"] = _Field.WaveguideSourceXY_modE_get
    if _newclass:
        modE = _swig_property(_Field.WaveguideSourceXY_modE_get, _Field.WaveguideSourceXY_modE_set)
    __swig_setmethods__["modH"] = _Field.WaveguideSourceXY_modH_set
    __swig_getmethods__["modH"] = _Field.WaveguideSourceXY_modH_get
    if _newclass:
        modH = _swig_property(_Field.WaveguideSourceXY_modH_get, _Field.WaveguideSourceXY_modH_set)
    __swig_setmethods__["Ex"] = _Field.WaveguideSourceXY_Ex_set
    __swig_getmethods__["Ex"] = _Field.WaveguideSourceXY_Ex_get
    if _newclass:
        Ex = _swig_property(_Field.WaveguideSourceXY_Ex_get, _Field.WaveguideSourceXY_Ex_set)
    __swig_setmethods__["Ey"] = _Field.WaveguideSourceXY_Ey_set
    __swig_getmethods__["Ey"] = _Field.WaveguideSourceXY_Ey_get
    if _newclass:
        Ey = _swig_property(_Field.WaveguideSourceXY_Ey_get, _Field.WaveguideSourceXY_Ey_set)
    __swig_setmethods__["Hx"] = _Field.WaveguideSourceXY_Hx_set
    __swig_getmethods__["Hx"] = _Field.WaveguideSourceXY_Hx_get
    if _newclass:
        Hx = _swig_property(_Field.WaveguideSourceXY_Hx_get, _Field.WaveguideSourceXY_Hx_set)
    __swig_setmethods__["Hy"] = _Field.WaveguideSourceXY_Hy_set
    __swig_getmethods__["Hy"] = _Field.WaveguideSourceXY_Hy_get
    if _newclass:
        Hy = _swig_property(_Field.WaveguideSourceXY_Hy_get, _Field.WaveguideSourceXY_Hy_set)

    def __init__(self, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12):
        this = _Field.new_WaveguideSourceXY(arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def a(self, arg2, arg3):
        return _Field.WaveguideSourceXY_a(self, arg2, arg3)

    def b(self, arg2, arg3):
        return _Field.WaveguideSourceXY_b(self, arg2, arg3)
    __swig_destroy__ = _Field.delete_WaveguideSourceXY
    __del__ = lambda self: None
WaveguideSourceXY_swigregister = _Field.WaveguideSourceXY_swigregister
WaveguideSourceXY_swigregister(WaveguideSourceXY)

# This file is compatible with both classic and new-style classes.


