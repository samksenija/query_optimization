from parameters import changes_applied, notes, layer_tags

queries = {
    "1_0": {
        "query": "SELECT * FROM orders where O_ORDERPRIORITY = '5-LOW' AND O_CUSTKEY = 1910;",
        "layer_tag": layer_tags[0],
        "change_applied": changes_applied[0],
        "note": notes[1]
    },
    "1_1": {
        "query": "SELECT * FROM orders where O_CUSTKEY = 1910 AND O_ORDERPRIORITY = '5-LOW';",
        "layer_tag": layer_tags[1],
        "change_applied": changes_applied[1],
        "note": notes[1]
    },
    "2_0": {
        "query": "SELECT * FROM orders WHERE O_ORDERKEY = 1858 AND O_ORDERSTATUS = 'O';",
        "layer_tag": layer_tags[0],
        "change_applied": changes_applied[0],
        "note": notes[2]
    },
    "2_1": {
        "query": "SELECT * FROM orders WHERE O_ORDERSTATUS = 'O' AND O_ORDERKEY = 1858;",
        "layer_tag": layer_tags[1],
        "change_applied": changes_applied[1],
        "note": notes[2]
    },
    "3_0": {
        "query": "SELECT * FROM orders WHERE O_ORDERKEY = 259 AND O_ORDERSTATUS = 'F';",
        "layer_tag": layer_tags[0],
        "change_applied": changes_applied[0],
        "note": notes[2]
    },
    "3_1": {
        "query": "SELECT * FROM orders WHERE O_ORDERSTATUS = 'F' AND O_ORDERKEY = 259;",
        "layer_tag": layer_tags[1],
        "change_applied": changes_applied[1],
        "note": notes[2]
    },
    "4_0": {
        "query": "SELECT * FROM orders WHERE O_ORDERKEY = 290 AND O_ORDERSTATUS = 'F';",
        "layer_tag": layer_tags[0],
        "change_applied": changes_applied[0],
        "note": notes[2]
    },
    "4_1": {
        "query": "SELECT * FROM orders WHERE O_ORDERSTATUS = 'F' AND O_ORDERKEY = 290 ;",
         "layer_tag": layer_tags[1],
        "change_applied": changes_applied[1],
        "note": notes[2]
    },
    "5_0": {
        "query": "SELECT * FROM orders WHERE O_ORDERSTATUS = 'F' AND O_ORDERKEY = 64;",
        "layer_tag": layer_tags[0],
        "change_applied": changes_applied[0],
        "note": notes[2]
    },
    "5_1": {
        "query": "SELECT * FROM orders WHERE O_ORDERKEY = 64 AND O_ORDERSTATUS = 'F';",
        "layer_tag": layer_tags[1],
        "change_applied": changes_applied[1],
        "note": notes[2]
    }
}