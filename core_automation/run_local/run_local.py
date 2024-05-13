from ..util import title, download_facts

def run_local(args):
    """
    Run the local core automation.
    """
    title()
    download_facts()
    print(args)