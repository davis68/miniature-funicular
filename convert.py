def dollars2cents ( dollars ):
    return dollars * 100

def cents2dollars ( cents ):
    return cents/100.0

def hours2mins ( hours ):
    return hours * 60

def cats2kittens ( cats ):
    import numpy
    return cats * numpy.floor(numpy.random.random()*10)
