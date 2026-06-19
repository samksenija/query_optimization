queries = {
    1: {
        "query": "SELECT * FROM orders where O_ORDERPRIORITY = '5-LOW' AND O_CUSTKEY = 1910;",
        "layer_tag": "original",
        "change_applied": None,
        "note": None
    },
    1: {
        "query": "SELECT * FROM orders where O_CUSTKEY = 1910 AND O_ORDERPRIORITY = '5-LOW';",
        "layer_tag": "1st",
        "change_applied": "Change of filter column order",
        "note": None
    }
}