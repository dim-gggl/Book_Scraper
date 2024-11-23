from script_phase_1 import (ROOT)
from script_phase_3 import scrape_all_categories


if __name__ == '__main__':
    scrape_all_categories(ROOT, keep_images=True)
