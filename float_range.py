import math

class float_range(object):
    
    def __init__(self, start, stop = None, step = 1.0):
        if stop == None:
            self.start, self.stop = 0.0, start
        else:
            self.start, self.stop = start, stop
            
        self.step = step
        
    def __iter__(self):        
        if self.step >= 0: 
            while self.start < self.stop:
                yield self.start
                self.start += self.step
        else:
            while self.start > self.stop:
                yield self.start
                self.start += self.step
            
    def __len__(self):
        if self.start > self.stop and self.step > 0:
            return 0
        if self.start < self.stop and self.step < 0:
            return 0
        
        return math.ceil((abs(self.stop - self.start))/abs(self.step))
    
    def __reversed__(self):        
        length = self.__len__()
        self.stop = self.start-self.step
        self.start = self.start+self.step*(length-1)        
        self.step = -self.step
        
        if self.step >= 0: 
            while self.start < self.stop:                
                yield self.start
                self.start += self.step
                
        else:
            while self.start > self.stop:
                yield self.start
                self.start += self.step
                
    def __eq__(self, other):
        
        if isinstance(other, (float_range, range)):
            
            lo = len(other)
            ls = len(self)
            
            if lo != ls:
                return False
            
            elif lo == 0 and  ls == 0:
                return True
            
            else:
                if (self.start + self.step) == (other.start + other.step):
                    return True
                
        return False
            