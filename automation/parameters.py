# Define the parameters for references, to be called dynamically
layer_tags = ["original", "1st", "2nd"]
changes_applied = [None, "Change of filter column order"]
notes = [
    None,
    "How filter order when no primary key is used affects the execution.", 
    """Primary key (O_ORDERKEY) is always index as well, so optimizator 
    will use it first when performing optimization, no matter where it's ordered in query."""
]