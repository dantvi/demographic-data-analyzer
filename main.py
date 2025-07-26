# This entrypoint file is used for local development and testing

import demographic_data_analyzer
from unittest import main

if __name__ == "__main__":
    # Call the main analysis function
    demographic_data_analyzer.calculate_demographic_data()

    # Run unit tests (you can enable/disable specific tests in test_module.py)
    main(module='test_module', exit=False)
