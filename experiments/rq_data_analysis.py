import os
import glob
import pandas as pd
import scienceplots
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


print('RQ3 experimental data analysis is started.')

dpi = 300
fontdict={'size': 14}
plot_dir = './exp_plot'

if os.path.isdir(plot_dir) is False:
    os.mkdir(plot_dir)

mono_csv_files = [
    'mono_convert_upload_retrieve_observation_scenario1_stats_history.csv',
    'mono_convert_upload_retrieve_procedure_scenario2_stats_history.csv',
    'mono_convert_upload_retrieve_medication_administration_data_scenario3_stats_history.csv',
    'mono_analyze_upload_retrieve_questionnaire_response_cdr_data_scenario4_stats_history.csv',
    'mono_convert_upload_retrieve_location_data_scenario5_stats_history.csv',
    'mono_convert_upload_retrieve_adverse_event_data_scenario6_stats_history.csv',
]
micro_csv_files = []
for csv_file in mono_csv_files:
    micro_csv_files += csv_file[5:],

xlabel = 'Timeline (s)'
ylabel = 'Total Average Response Time'

for index,csv_file in enumerate(mono_csv_files):
    mono_csv_file = csv_file
    micro_csv_file = micro_csv_files[index]

    mono_history = pd.read_csv(mono_csv_file)
    mono_history['Timestamp'] = pd.to_datetime(mono_history['Timestamp'], unit='s')

    micro_history = pd.read_csv(micro_csv_file)
    micro_history['Timestamp'] = pd.to_datetime(micro_history['Timestamp'], unit='s')

    print(f'Processing and Drawing the RQ3 {csv_file} data.')

    with plt.style.context(['science', 'ieee', 'no-latex']):
        fig, ax = plt.subplots()
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))

        length = min(len(mono_history['Timestamp']), len(micro_history['Timestamp']))

        ax.plot(
            range(0, length),
            mono_history['Total Average Response Time'][0:length],
            label='monolith', color='blue', ls='-', marker=''
        )
        ax.plot(
            range(0, length),
            micro_history['Total Average Response Time'][0:length],
            label='microservice', color='orange', ls='-', marker='')

        ax.legend()

        ax.set_xlabel(xlabel, fontdict=fontdict)
        ax.set_ylabel(ylabel, fontdict=fontdict)

        fig.savefig(f'{plot_dir}/fig_rq3_scenario{index+1}_result.svg', dpi=dpi)
        fig.savefig(f'{plot_dir}/fig_rq3_scenario{index+1}_result.png', dpi=dpi)
        plt.close()


    print(f'RQ3 experimental {mono_csv_file} data analysis is finished.')
    print(f'RQ3 experimental {micro_csv_file} data analysis is finished.')
