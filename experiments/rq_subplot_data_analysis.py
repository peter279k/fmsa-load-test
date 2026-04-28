import os
import glob
import pandas as pd
import scienceplots
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


print('RQ3 experimental data analysis is started (subplots).')

dpi = 300
fontdict={'size': 15}
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
titles = [['a', 'b', 'c'], ['d', 'e', 'f']]

for scenario,csv_files in mono_csv_files.items():
    micro_csv_files[scenario] = []
    for csv_file in csv_files:
        micro_csv_files[scenario] += csv_file[5:],


xlabel = 'Timeline (s)'

for scenario,csv_files in mono_csv_files.items():
    with plt.style.context(['science', 'ieee', 'no-latex']):
        fig, axs = plt.subplots(nrows=2, ncols=3, layout='constrained', figsize=(9, 4))

        for index in range(0, 2):
            for num in range(0, 3):
                mono_history = pd.read_csv(csv_files[num])
                micro_history = pd.read_csv(micro_csv_files[scenario][num])

                ylabel = 'Total Failure Count'
                if index == 1:
                    ylabel = 'Average Response Time'

                length = min(len(mono_history['Timestamp']), len(micro_history['Timestamp']))
                lengths = range(0, length)

                failure_counts = list(mono_history[ylabel].tolist())
                failure_counts.extend(list(micro_history[ylabel].tolist()))

                failure_length = max(failure_counts)

                axs[index, num].xaxis.set_major_locator(MaxNLocator(integer=True))
                axs[index, num].yaxis.set_major_locator(MaxNLocator(integer=True))

                axs[index, num].set_xlim(0, length)
                axs[index, num].set_ylim(0, failure_length)

                axs[index, num].plot(
                    lengths,
                    mono_history[ylabel][0:length],
                    label='monolith', color='blue', ls='-', marker=''
                )
                axs[index, num].plot(
                    lengths,
                    micro_history[ylabel][0:length],
                    label='microservice', color='orange', ls='-', marker=''
                )

                axs[index, num].set_ylabel(ylabel)

                axs[index, num].set_title(titles[index][num], y=-0.2)

                axs[index, num].legend()

        fig.supxlabel('Timeline(s)')
        fig.suptitle(f'S{scenario[1:]}', fontsize=15)

        fig.savefig(f'{plot_dir}/fig_rq3_{scenario}_result.svg', dpi=dpi)
        fig.savefig(f'{plot_dir}/fig_rq3_{scenario}_result.png', dpi=dpi)

        plt.close()

        print(f'RQ3 experimental {scenario} data analysis (subplots) is finished.\n')
