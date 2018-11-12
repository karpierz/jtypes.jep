__import__("jvm._util", globals(), None, ["make_config"], 2).make_config("jep.cfg", "jt.jep")

def have_numpy():
    try:
        import numpy
        return True
    except ImportError:  # pragma: no cover
        return False
