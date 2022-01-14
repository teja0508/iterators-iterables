
from Polygon import Polygon 
class Polygon_Sequence :
        
        """
        Implementaion Of Custom Sequence of Polygons which takes
        largest polygon num of edges and circumradius as input
        """
    
        def __init__(self, num_edges : int , circumradius : float) -> None :
            
            self._largest_num_edges = num_edges
            self._circumradius = circumradius
            self._polygons = []
            
        def __repr__(self) : 
            return f'Polygon Sequence::  Circumradius : {self.circumradius} , Largest Number Of Edges: {self.largest_num_edges}, length : {self.__len__()}'
       
    
        def __iter__(self):
            
            return self.PolygonIterator(self)

        @property
        def largest_num_edges(self):
            return self._largest_num_edges
        
        @largest_num_edges.setter
        def largest_num_edges(self, value):
            if value < 3:
                raise ValueError("The number of vertices should be more than 3")
                
            self._largest_num_edges = value
            
        @property    
        def circumradius(self):

            return self._circumradius

        @circumradius.setter
        def circumradius(self, value):

            if(value < 0) : 
                raise ValueError(" Radius should be greater than 0")
            self._circumradius = value
            
        def __len__(self):
            return self.largest_num_edges - 2
            
        def __getitem__(self, pos):
            
            if isinstance(pos, int):
                if pos < 0:
                    pos = self.largest_num_edges - 2 + pos
                if pos < 0 or pos >=(self.largest_num_edges - 2):
                    raise IndexError
                else:
                    return self._polygon(pos + 3)
            else:
                start, stop, step = pos.indices(self.largest_num_edges-2)
                rng = range(start, stop, step)
                return [self._polygon(i+3) for i in rng]
            
        def _polygon(self,num_edges) :
            
            return Polygon(num_edges,self.circumradius)
        
        @property
        def max_efficiency_polygon(self):
            sorted_polygons = sorted(self, key = lambda polygon: polygon.area/polygon.perimeter, reverse = True)
            return sorted_polygons[0]
        
        class PolygonIterator:
            def __init__(self, poly_obj):

                self._poly_obj = poly_obj
                self._index = 3

            def __iter__(self):
                return self

            def __next__(self):

                if self._index > self._poly_obj.largest_num_edges:
                    raise StopIteration
                else:

                    poly = Polygon(self._index, self._poly_obj._circumradius)
                    self._index += 1
                    return poly
      