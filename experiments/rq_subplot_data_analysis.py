import os
import glob
import pandas as pd
import scienceplots
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


print('RQ3 experimental data analysis is started (subplots).')

dpi = 300
fontdict={'size': 12}
plot_dir = './exp_plot'

if os.path.isdir(plot_dir) is False:
    os.mkdir(plot_dir)


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
        'mono_analyze_only_upload_retrieve_questionnaire_response_cdr_data_scenario4_stats_history.csv'
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
    micro_csv_files[scenario] = list(csv_files)


xlabel = 'Timeline (s)'

for scenario,csv_files in mono_csv_files.items():
    mono_histories = []
    micro_histories = []
    print(f'Drawing the {scenario} subplot')

    for index,csv_file in enumerate(csv_files):
        mono_csv_file = csv_file
        micro_csv_file = micro_csv_files[scenario][index]

        mono_history = pd.read_csv(mono_csv_file)
        mono_history['Timestamp'] = pd.to_datetime(mono_history['Timestamp'], unit='s')

        micro_history = pd.read_csv(micro_csv_file)
        micro_history['Timestamp'] = pd.to_datetime(micro_history['Timestamp'], unit='s')

        mono_histories += mono_history,
        micro_histories += micro_history,

    with plt.style.context(['science', 'ieee', 'no-latex']):
        fig, axs = plt.subplots(nrows=2, ncols=3)
        axs.xaxis.set_major_locator(MaxNLocator(integer=True))
        axs.yaxis.set_major_locator(MaxNLocator(integer=True))

        for index, mono_history in enumerate(mono_histories):
            length = min(len(mono_history['Timestamp']), len(micro_history[index]['Timestamp']))
            lengths = range(0, length)
            for num in range(0, 3):
                axs[0, num].plot(
                    lengths,
                    mono_history['Total Failure Count'][0:length],
                    label='monolith', color='blue', ls='-', marker=''
                )
                axs[0, num].plot(
                    lengths,
                    micro_history['Total Failure Count'][0:length],
                    label='microservice', color='orange', ls='-', marker=''
                )

                axs[0, num].legend()

                axs[0, num].set_xlabel(xlabel, fontdict=fontdict)
                axs[0, num].set_ylabel('Total Failure Count', fontdict=fontdict)

                axs[1, num].plot(
                    lengths,
                    mono_history['Total Average Response Time'][0:length],
                    label='monolith', color='blue', ls='-', marker=''
                )
                axs[1, num].plot(
                    lengths,
                    micro_history['Total Average Response Time'][0:length],
                    label='microservice', color='orange', ls='-', marker=''
                )

                axs[1, num].legend()

                axs[1, num].set_xlabel(xlabel, fontdict=fontdict)
                axs[1, num].set_ylabel('Total Average Response Time', fontdict=fontdict)

        fig.savefig(f'{plot_dir}/fig_rq3_scenario{index+1}_result.svg', dpi=dpi)
        fig.savefig(f'{plot_dir}/fig_rq3_scenario{index+1}_result.png', dpi=dpi)
        plt.close()

        print(f'RQ3 experimental {mono_csv_file} and {micro_csv_file} data analysis (subplots) is finished.')
