def PrintProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = " "):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

def memoize(f): 
    # answers[args] = f(*args)
    answers = {}
    def wrapper(*args):
        if args not in answers:
            answers[args] = f(*args)
        return answers[args]
    return wrapper

# def memoize_dijkstra(f):
#     # This should only be used when args are dicts. 
#     # answers[args] = f(*args)
#     answers = {}
#     def wrapper(*args):
#         if args[0].values() not in answers:
#             print(args[0])
#             answers[args] = f(*args)
#         return answers[args]
#     return wrapper

# # @memoize2
# # def my_func(x):
# #     return x + 15

# # my_func(3,5)
# # my_func(3,3)

# @memoize_dijkstra
# def my_func_dict(dic):
#     return sum(list(dic.values()))

# my_dict = {'a': 2, 'b': 4}

# my_func_dict(my_dict)
