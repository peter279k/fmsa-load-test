import os
import glob
import pandas as pd
import scienceplots
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


print('RQ3 experimental data analysis is started (subplots).')

dpi = 300
fontdict={'size': 10}
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

        micro_history = pd.read_csv(micro_csv_file)

        mono_histories += mono_history,
        micro_histories += micro_history,

    with plt.style.context(['science', 'ieee', 'no-latex']):
        fig, axs = plt.subplots(nrows=2, ncols=3)

        for index in range(0, 2):
            if index == 0:
                ylabel = 'Total Failure Count'
            else:
                ylabel = 'Total Average Response Time'

            for j in range(0, 3):
                length = min(len(mono_histories[j]['Timestamp']), len(micro_histories[j]['Timestamp']))
                lengths = range(0, length)

                axs[index, j].xaxis.set_major_locator(MaxNLocator(integer=True))
                axs[index, j].yaxis.set_major_locator(MaxNLocator(integer=True))

                axs[index, j].plot(
                    lengths,
                    mono_histories[0][ylabel][0:length],
                    label='monolith', color='blue', ls='-', marker=''
                )
                axs[index, j].plot(
                    lengths,
                    micro_histories[0][ylabel][0:length],
                    label='microservice', color='orange', ls='-', marker=''
                )

                axs[index, j].legend()

                axs[index, j].set_xlabel(xlabel, fontdict=fontdict)
                axs[index, j].set_ylabel(ylabel, fontdict=fontdict)

        plt.tight_layout()

        fig.savefig(f'{plot_dir}/fig_rq3_scenario{index+1}_result.svg', dpi=dpi)
        fig.savefig(f'{plot_dir}/fig_rq3_scenario{index+1}_result.png', dpi=dpi)
        plt.close()

        print(f'RQ3 experimental {mono_csv_file} and {micro_csv_file} data analysis (subplots) is finished.\n')
