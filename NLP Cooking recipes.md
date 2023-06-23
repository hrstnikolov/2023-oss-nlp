# NLP Cooking Recipes


## Detailed description of each step
1. Download and preprocess cooking recipes.
1. Assign 384-dimension vector to each recipe so that similar recipes have similar vectors.
1. Convert the 384-dimension vector to 2D vector i.e. x and y coords.
1. Create an interactive plot to visualize the 2D representations of the recipes.
1. Create function that takes a new recipe and returns the most similar 5pcs recipes (e.g. IN: Pork chops, OUT: Pork Cutlets, Breaded Pork Chops, Beef Chops...).



## Generalized procedure
1. get data
1. make embeddings
1. dimensionality reduction
1. visualize interactively
1. simple semantic search


## How / tool used / implementation
1. Download zip files from ?. Unzip json files and concatenate them. Lightly clean the data.
1. `SentenceTransformers`, use the `all-MiniLM-L6-v2` model.
1. From the `umap` module use the `UMAP` class. Another option: TruncatedSVD.
1. Use `Bulk` although other several libraries are available ( `altair`, `bokeh`, `plotly`). 

