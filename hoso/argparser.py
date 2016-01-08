import argparse

parser = argparse.ArgumentParser(
    description = "Hoso is a braoadcasting tool that allows you to post status updates to multiple social media networks at the same time"
)

parser.add_argument(
    "-m",
    "--message",
    default = None, help = "Your status update. You will be prompted inside the program if this is not specified"
)

parser.add_argument(
    "-c",
    "--channels",
    default = None,
    help = "A list of social networks you wish to post to. You will be prompted inside the program if this is not specified",
    nargs = '+'
)

args = parser.parse_args()
