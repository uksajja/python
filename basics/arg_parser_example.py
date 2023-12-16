import argparse
import multiprocessing

def main():
    parser = argparse.ArgumentParser(prog = "ParserExample", description = "Parsing Commandline Arguments")
    parser.add_argument('-n', default = multiprocessing.cpu_count(), type = int)
    parser.add_argument('-c', "--count",  action='count', dest='num')
    parser.add_argument("--sum", default=sum, const = sum, action='store_const', dest = 'total')
    args = parser.parse_args()
    print(args)
    num_threads = args.n
    print(f"number of threads: {num_threads}")


if __name__=="__main__":
    main()