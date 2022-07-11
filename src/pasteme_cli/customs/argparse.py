def line_range_type(rng) -> str:
    return rng.split('-')
    # print(re.findall(r'(\d.*-\d.*)', rng))
    # if not re.match(r'(\d.*)-(\d.*)', rng):
    #     return None
    # else:
    #     return rng.split('-')
    
    # TODO: needs optimizations (using regex)