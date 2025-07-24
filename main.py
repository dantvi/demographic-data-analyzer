# This entrypoint file is used for local development and testing
import demographic_data_analyzer

# Run the main function to verify local setup
if __name__ == "__main__":
    # Call function with print_data=True to show output
    demographic_data_analyzer.calculate_demographic_data()

    # Disable tests for now during setup phase
    # from unittest import main
    # main(module='test_module', exit=False)
