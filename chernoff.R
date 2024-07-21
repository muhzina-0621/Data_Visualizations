install.packages("aplpack")#comment this line after installing
# Load the aplpack package
library(aplpack)


data <- matrix(
  c(
    4.0, 3.0, 2.0, 5.0, 3.5, 4.5,
    3.0, 2.5, 4.5, 3.0, 4.0, 2.0,
    5.0, 4.5, 3.0, 2.0, 4.5, 3.5,
    2.0, 3.5, 5.0, 4.0, 2.5, 4.0,
    4.5, 3.0, 4.0, 3.5, 5.0, 3.0
  ),
  nrow = 5,
  byrow = TRUE
)

# Generate Chernoff faces
faces(data, face.type=0)
