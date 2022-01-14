
# Polygon.py


import math

class Polygon :
    
    """
    Implementation of a regular Polygon which takes num_eges and circumradius as input
    It can give num_eges, num_vertices,interior angle,edge length,apothem,area,perimeter
    
    """
    
    def __init__(self, num_edges : int, circumradius : float) -> None:
    
        self.num_edges =  num_edges
        self.circumradius = circumradius
        
    @property
    def num_edges(self):
       
 
        return self._num_edges
    
    @num_edges.setter
    def num_edges(self, value):
        
        if not isinstance(value, int):
            raise TypeError("Number of edges/ vertices must be an integer.")
   
        if(value < 3):
            raise ValueError("Polygon should have atleast 3 edges")
            
        self._num_edges = value
        self._num_vertices = value
        self._interior_angle = None
        self._edge_length = None
        self._apothem = None
        self._area = None
        self._perimeter = None
    
    @property
    def num_vertices(self):

        
        return self._num_edges
    
    @num_vertices.setter
    def num_vertices(self, value):
        if not self._num_vertices : 
            self._num_vertices = self.num_edges
        return self._num_vertices
        
        
       
    @property    
    def circumradius(self):
        
        return self._circumradius
    
    @circumradius.setter
    def circumradius(self, value):
        
        if(value < 0) : 
            raise ValueError(" Radius should be greater than 0")
        self._circumradius = value

    @property  
    def interior_angle(self):
        
        if not self._interior_angle:
            self._interior_angle = (self.num_edges - 2) * 180 / self.num_edges
        return self._interior_angle
    
    @property  
    def edge_length(self):
        
        if not self._edge_length:
            self._edge_length = 2 * self.circumradius * math.sin(math.pi/ self.num_edges)
            
        return self._edge_length
    
    @property  
    def apothem(self):
        
        if not self._apothem:
            self._apothem = self.circumradius * math.cos(math.pi/ self.num_edges)
        return self._apothem
    
    @property  
    def area(self):
        if not self._area : 
            self._area = 1/2 * self.num_edges * self.edge_length * self.apothem
            
        return self._area
    
    @property  
    def perimeter(self):
        
        if not self._perimeter :
            self._perimeter = self.num_edges * self.edge_length
        return self._perimeter

    
    def __repr__(self) : 
        return  f"Regular Convex Polygon with edges : {self.num_edges} and circumradius : {self.circumradius}"
    
    def __eq__(self, other):
        
        if isinstance(other, Polygon):
        
            return self.num_edges == other.num_edges and self.circumradius == other.circumradius
        
        else:
            raise TypeError("Expected Type Polygon")
    
    def __gt__(self, other) :
                            
          if isinstance(other, Polygon):
                            
            return self.num_vertices > other.num_vertices
           
          else : 
                raise TypeError("Expected Type Polygon")