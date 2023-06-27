from yellowbrick.features import ParallelCoordinates  
visualizer = ParallelCoordinates()
visualizer.fit_transform(X, y) 
visualizer.show()
