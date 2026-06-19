queries = {
    "1_0": {
        "query": "SELECT * FROM orders where O_ORDERPRIORITY = '5-LOW' AND O_CUSTKEY = 1910;",
        "layer_tag": "original",
        "change_applied": None,
        "note": None
    },
    "1_1": {
        "query": "SELECT * FROM orders where O_CUSTKEY = 1910 AND O_ORDERPRIORITY = '5-LOW';",
        "layer_tag": "1st",
        "change_applied": "Change of filter column order",
        "note": None
    },
    "2_0": {
        "query": "SELECT * FROM orders WHERE O_ORDERKEY = 1858 AND O_ORDERSTATUS = 'O';",
        "layer_tag": "original",
        "change_applied": None,
        "note": None
    },
    "2_1": {
        "query": "SELECT * FROM orders WHERE O_ORDERSTATUS = 'O' AND O_ORDERKEY = 1858;",
        "layer_tag": "1st",
        "change_applied": "Change of filter column order",
        "note": None
    },
    "3_0": {
        "query": "SELECT * FROM orders WHERE O_ORDERKEY = 259 AND O_ORDERSTATUS = 'F';",
        "layer_tag": "original",
        "change_applied": None,
        "note": None
    },
    "3_1": {
        "query": "SELECT * FROM orders WHERE O_ORDERSTATUS = 'F' AND O_ORDERKEY = 259;",
        "layer_tag": "1st",
        "change_applied": "Change of filter column order",
        "note": None
    },
    "4_0": {
        "query": "SELECT * FROM orders WHERE O_ORDERKEY = 290 AND O_ORDERSTATUS = 'F';",
        "layer_tag": "original",
        "change_applied": None,
        "note": None
    },
    "4_1": {
        "query": "SELECT * FROM orders WHERE O_ORDERSTATUS = 'F' AND O_ORDERKEY = 290 ;",
        "layer_tag": "1st",
        "change_applied": "Change of filter column order",
        "note": None
    },
    "5_0": {
        "query": "SELECT * FROM orders WHERE O_ORDERSTATUS = 'F' AND O_ORDERKEY = 64;",
        "layer_tag": "original",
        "change_applied": None,
        "note": None
    },
    "5_1": {
        "query": "SELECT * FROM orders WHERE O_ORDERKEY = 64 AND O_ORDERSTATUS = 'F';",
        "layer_tag": "1st",
        "change_applied": "Change of filter column order",
        "note": None
    }
}