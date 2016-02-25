class Argparser():

    def argParser(self):

        import argparse

        parser = argparse.ArgumentParser(description='Apache2 log parser')
        parser.add_argument('--path', help='Path to Apache2 log files', default="/logs")
        parser.add_argument('--top-urls', help="Find top URL-s", action='store_true')
        parser.add_argument('--geoip', help="Resolve IP-s to country codes", action='store_true')

        args = parser.parse_args()
        print("We are expecting logs from:", args.path)
        print("Do we want top URL-s?")
