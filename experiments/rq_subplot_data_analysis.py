import os
import glob
import pandas as pd
import scienceplots
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator, PercentFormatter


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
        'mono_convert_only_upload_retrieve_location_data_scenario4_stats_history.csv',
        'mono_convert_upload_only_retrieve_location_data_scenario4_stats_history.csv',
        'mono_convert_upload_retrieve_location_data_scenario4_stats_history.csv',
    ],
    'scenario5': [
        'mono_convert_only_upload_retrieve_adverse_event_data_scenario5_stats_history.csv',
        'mono_convert_upload_only_retrieve_adverse_event_data_scenario5_stats_history.csv',
        'mono_convert_upload_retrieve_adverse_event_data_scenario5_stats_history.csv',
    ],
}

micro_csv_files = {}
real_mono_csv_files = {}
titles = [['a', 'b', 'c'], ['d', 'e', 'f']]

for scenario,csv_files in mono_csv_files.items():
    micro_csv_files[scenario] = []
    real_mono_csv_files[scenario] = []
    for csv_file in csv_files:
        micro_csv_files[scenario] += csv_file[5:],
        real_mono_csv_files[scenario] += f'real_{csv_file}',


xlabel = 'Timeline (s)'

for scenario,csv_files in mono_csv_files.items():
    with plt.style.context(['science', 'ieee', 'no-latex']):
        fig, axs = plt.subplots(nrows=2, ncols=3, layout='constrained', figsize=(9, 4))

        for index in range(0, 2):
            for num in range(0, 3):
                mono_history = pd.read_csv(csv_files[num])
                micro_history = pd.read_csv(micro_csv_files[scenario][num])
                real_mono_history = pd.read_csv(real_mono_csv_files[scenario][num])

                if index == 0:
                    ylabel = 'Cumulative Failure Rate'
                    y_label = 'Cumulative Failure Rate'
                else:
                    ylabel = 'Total Average Response Time'
                    y_label = 'Average Response Time (ms)'

                mono_history['Timestamp'] = pd.to_datetime(mono_history['Timestamp'], unit='s')
                mono_history = mono_history.set_index('Timestamp')
                mono_history = mono_history.resample('1s').mean(numeric_only=True).ffill()
                mono_history['Cumulative Failure Rate'] = (
                    mono_history['Total Failure Count'] / mono_history['Total Request Count']
                ).fillna(0)

                micro_history['Timestamp'] = pd.to_datetime(micro_history['Timestamp'], unit='s')
                micro_history = micro_history.set_index('Timestamp')
                micro_history = micro_history.resample('1s').mean(numeric_only=True).ffill()
                micro_history['Cumulative Failure Rate'] = (
                    micro_history['Total Failure Count'] / micro_history['Total Request Count']
                ).fillna(0)

                real_mono_history['Timestamp'] = pd.to_datetime(real_mono_history['Timestamp'], unit='s')
                real_mono_history = real_mono_history.set_index('Timestamp')
                real_mono_history = real_mono_history.resample('1s').mean(numeric_only=True).ffill()
                real_mono_history['Cumulative Failure Rate'] = (
                    real_mono_history['Total Failure Count'] / real_mono_history['Total Request Count']
                ).fillna(0)

                length = min(
                    len(mono_history[ylabel].to_list()),
                    len(micro_history[ylabel].to_list()),
                    len(real_mono_history[ylabel].to_list()),
                )
                lengths = range(length)

                axs[index, num].xaxis.set_major_locator(MaxNLocator(integer=True))

                axs[index, num].set_xlim(0, 1200)

                if index == 0:
                    # Scale the axis to the maximum failure rate observed,
                    # leaving some headroom so the line does not touch the top.
                    failure_rates = list(mono_history[ylabel].tolist())
                    failure_rates.extend(list(micro_history[ylabel].tolist()))
                    failure_rates.extend(list(real_mono_history[ylabel].tolist()))

                    max_failure_rate = max(failure_rates)

                    top = max_failure_rate * 1.1
                    if top <= 0:
                        # No failures at all: use a small span so the flat
                        # line at 0% is drawn against a readable axis.
                        top = 0.01
                    # Small margin below 0 so a line sitting at 0% stays
                    # visible instead of hiding on the bottom axis.
                    bottom = -top * 0.05
                    axs[index, num].set_ylim(bottom, top)
                    axs[index, num].yaxis.set_major_formatter(PercentFormatter(xmax=1))
                else:
                    axs[index, num].yaxis.set_major_locator(MaxNLocator(integer=True))

                    failure_counts = list(mono_history[ylabel].tolist())
                    failure_counts.extend(list(micro_history[ylabel].tolist()))
                    failure_counts.extend(list(real_mono_history[ylabel].tolist()))

                    failure_length = max(failure_counts)
                    if int(failure_length) == 0:
                        failure_length = 1
                    axs[index, num].set_ylim(0, failure_length)

                line_vmsa, = axs[index, num].plot(
                    lengths,
                    mono_history[ylabel][0:length],
                    label='V-MSA', color='blue', ls='-',
                    marker='o', markevery=(0, 150), markersize=3.5
                )
                line_hmsa, = axs[index, num].plot(
                    lengths,
                    micro_history[ylabel][0:length],
                    label='H-MSA', color='orange', ls='--',
                    marker='s', markevery=(50, 150), markersize=3.5
                )
                line_mono, = axs[index, num].plot(
                    lengths,
                    real_mono_history[ylabel][0:length],
                    label='MONO', color='red', ls=':',
                    marker='^', markevery=(100, 150), markersize=3.5
                )

                if index == 0 and num == 0:
                    axs[index, num].set_ylabel(y_label, fontsize=11)
                if index == 1 and num == 0:
                    axs[index, num].set_ylabel(y_label, fontsize=11)

                axs[index, num].set_title(f'({titles[index][num]})', y=-0.4)

        # One shared legend outside the six subplots, placed at the top-left
        # so it does not overlap the centered S{n} title.
        fig.legend(
            handles=[line_mono, line_hmsa, line_vmsa],
            loc='outside upper left', ncol=3
        )

        fig.supxlabel(xlabel, fontsize=11)
        fig.suptitle(f'S{scenario[1:]}', fontsize=15)

        fig.savefig(f'{plot_dir}/fig_rq3_{scenario}_result.svg', dpi=dpi)
        fig.savefig(f'{plot_dir}/fig_rq3_{scenario}_result.png', dpi=dpi)

        plt.close()

        print(f'RQ3 experimental {scenario} data analysis (subplots) is finished.\n')
