import pandas as pd
from datetime import datetime


mono_csv_files = {
    'scenario1': [
        'mono_convert_only_upload_retrieve_observation_scenario1_stats_history.csv',
        'mono_convert_upload_only_retrieve_observation_scenario1_stats_history.csv',
        'mono_convert_upload_retrieve_observation_scenario1_stats_history.csv',
    ],
    'scenario2': [
        'mono_convert_only_upload_retrieve_procedure_scenario2_stats_history.csv',
        'mono_convert_upload_only_retrieve_procedure_scenario2_stats_history.csv',
        'mono_convert_upload_retrieve_procedure_scenario2_stats_history.csv',
    ],
    'scenario3': [
        'mono_convert_only_upload_retrieve_medication_administration_data_scenario3_stats_history.csv',
        'mono_convert_upload_only_retrieve_medication_administration_data_scenario3_stats_history.csv',
        'mono_convert_upload_retrieve_medication_administration_data_scenario3_stats_history.csv',
    ],
    'scenario4': [
        'mono_analyze_only_upload_retrieve_questionnaire_response_cdr_data_scenario4_stats_history.csv',
        'mono_analyze_upload_only_retrieve_questionnaire_response_cdr_data_scenario4_stats_history.csv',
        'mono_analyze_upload_retrieve_questionnaire_response_cdr_data_scenario4_stats_history.csv',
    ],
    'scenario5': [
        'mono_convert_only_upload_retrieve_location_data_scenario5_stats_history.csv',
        'mono_convert_upload_only_retrieve_location_data_scenario5_stats_history.csv',
        'mono_convert_upload_retrieve_location_data_scenario5_stats_history.csv',
    ],
    'scenario6': [
        'mono_convert_only_upload_retrieve_adverse_event_data_scenario6_stats_history.csv',
        'mono_convert_upload_only_retrieve_adverse_event_data_scenario6_stats_history.csv',
        'mono_convert_upload_retrieve_adverse_event_data_scenario6_stats_history.csv',
    ],
}

micro_csv_files = {}

for scenario,csv_files in mono_csv_files.items():
    micro_csv_files[scenario] = []
    for index,csv_file in enumerate(csv_files):
        micro_csv_files[scenario] += csv_file.replace('_history', '')[5:],
        mono_csv_files[scenario][index] = csv_file.replace('_history', '')

for scenario, csv_files in mono_csv_files.items():
    for index, csv_file in enumerate(csv_files):
        stats = pd.read_csv(csv_file)
        total = stats[stats['Name'] == 'Aggregated'].iloc[0]

        print(f'\n### Overall {csv_file} Summary ###')
        print(f"Failure Rate: {total['Failure Count']/total['Request Count']*100:.2f}%")
        print(f"Average Response Time: {total['Average Response Time']:.0f}ms")

        stats = pd.read_csv(micro_csv_files[scenario][index])
        total = stats[stats['Name'] == 'Aggregated'].iloc[0]

        print(f'\n### Overall {micro_csv_files[scenario][index]} Summary ###')
        print(f"Failure Rate: {total['Failure Count']/total['Request Count']*100:.2f}%")
        print(f"Average Response Time: {total['Average Response Time']:.0f}ms")
