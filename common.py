CLASSES       = ["RM50"]
CLASS = {
    "RM50" : "0",
}
CHANNEL     = 3

GRID_WIDTH  = int(8) # The size of 1 cell.
GRID_HEIGHT = int(8)
WIDTH       = int(64)
HEIGHT      = int(64)
GRID_X      = WIDTH // GRID_WIDTH # The number of cells.
GRID_Y      = HEIGHT // GRID_HEIGHT


# Training parameters
SAMPLE = 100
BATCH  = 8
EPOCH  = 100

# Inference parameters
DETECTION_PARAMETER = 0.9
NMS = 0.1


# Generator parameters
money_path = "cash/"
validation_path = "data/val/"
test_path = "data/test/"




# CLASS_INDEX = ["RM50", "RM1", "RM10", "RM20","RM100"]

