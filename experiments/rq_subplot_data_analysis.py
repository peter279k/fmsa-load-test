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

for scenario,csv_files in mono_csv_files.items():
    micro_csv_files[scenario] = list(csv_files)


xlabel = 'Timeline (s)'

for scenario,csv_files in mono_csv_files.items():
    with plt.style.context(['science', 'ieee', 'no-latex']):
        fig, axs = plt.subplots(nrows=2, ncols=3, layout='constrained', figsize=(5.5, 3.5))

        for num in range(0, 3):
            mono_history = pd.read_csv(csv_files[num])
            micro_history = pd.read_csv(csv_files[num])

            ylabel = 'Total Failure Count'

            length = min(len(mono_history['Timestamp']), len(micro_history['Timestamp']))
            lengths = range(0, length)

            axs[0, num].xaxis.set_major_locator(MaxNLocator(integer=True))
            axs[0, num].yaxis.set_major_locator(MaxNLocator(integer=True))

            axs[0, num].plot(
                lengths,
                mono_history[ylabel][0:length],
                label='monolith', color='blue', ls='-', marker=''
            )
            axs[0, num].plot(
                lengths,
                micro_history[ylabel][0:length],
                label='microservice', color='orange', ls='-', marker=''
            )

            axs[0, num].legend()

            for ax in axs.flat:
                ax.set(xlabel=xlabel, ylabel=ylabel)

            for ax in axs.flat:
                ax.label_outer()

        fig.savefig(f'{plot_dir}/fig_rq3_{scenario}_result.svg', dpi=dpi)
        fig.savefig(f'{plot_dir}/fig_rq3_{scenario}_result.png', dpi=dpi)

        plt.close()

        print(f'RQ3 experimental {scenario} data analysis (subplots) is finished.\n')
