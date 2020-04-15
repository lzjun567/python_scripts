{"query": {"function_score": {"query": {
    "bool": {"should": [{"multi_match": {"query": "python", "fields": ["nickname^2", "username^4"]}}],
             "filter": {"range": {"follower_count": {"gte": "50000", "lte": "100000"}}}}},
    "field_value_factor": {"field": "follower_count", "modifier": "log1p", "missing": 0,
                           "factor": 1}, "boost_mode": "avg"}},
    "highlight": {"fields": {"nickname": {}, "description": {}}}, "size": 10, "from": 0}





{
        "query": {
            "function_score": {
                "query": {
                    "bool": {"must": [{
                        "multi_match": {
                            "query": "python",
                            "fields": ["nickname^2", "username^4"]
                        }}],
                        "filter": {"range": {
                            "follower_count": {
                                "gte": "50000",
                                "lte": "100000"
                            }
                        }}}
                },

                "field_value_factor": {
                    "field": "follower_count",
                    "modifier": "log1p",
                    "missing": 0,
                    "factor": 1
                },

                "boost_mode": "avg"
            }
        },
        "highlight": {
            "fields": {
                "nickname": {},
                "description": {}
            }
        },
        "size":10,
        "from": 0
    }