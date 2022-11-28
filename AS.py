import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scienceplots
import seaborn as sns
c=sns.color_palette("rainbow", as_cmap=True)



plt.style.use(['science','nature','bright'])
plt.rcParams["figure.autolayout"]=True





dados_df = pd.read_csv('dados.csv')
bindingEn=np.array(dados_df["BE_dados_as.dat"])
background=np.array(dados_df["Background_dados_as.dat"])
counts_tot=np.array(dados_df["CPS_dados_as.dat"])
counts_Si4_3_2=np.array(dados_df["SiO2 3/2_1_dados_as.dat"])
counts_Si4_1_2=np.array(dados_df["SiO2 1/2_2_dados_as.dat"])
counts_Si0_3_2=np.array(dados_df["Si 3/2_3_dados_as.dat"])
counts_Si0_1_2=np.array(dados_df["Si 1/2_4_dados_as.dat"])
counts_Si1_3_2=np.array(dados_df["Si 1+ 3/2_5_dados_as.dat"])
counts_Si1_1_2=np.array(dados_df["Si 1+ 1/2_6_dados_as.dat"])
counts_Si3_3_2=np.array(dados_df["Si 3+ 3/2_7_dados_as.dat"])
counts_Si3_1_2=np.array(dados_df["Si 3+ 1/2_8_dados_as.dat"])
residuals=np.array(dados_df["Normalised_Residual_dados_as.dat"])

fig0,ax0=plt.subplots()


ax0.invert_xaxis()
ax0.set_xlabel('Binding Energy (eV)')
ax0.set_ylabel('Arbitrary Units')
ax0.set_ylabel('Arbitrary Units')


ax0.plot(bindingEn,counts_tot,'.',label='Data')
ax0.plot(bindingEn,background,label='Shirley Background')
ax0.plot(bindingEn,counts_tot-background,'.',label='Data without background')

ax0.legend()
ax0.grid()




fig1,ax1=plt.subplots(2,1,sharex=True,gridspec_kw={'height_ratios': [5, 1]})


fig1.set_figheight(4)
fig1.subplots_adjust(hspace=0.2)
ax0.invert_xaxis()

ax1[0].plot(bindingEn[::5],counts_tot[::5]-background[::5],'.',label='Data (undersampled)')
color = next(ax1[0]._get_lines.prop_cycler)['color']
ax1[0].plot(bindingEn,counts_Si0_3_2-background,c=color,label='Si 2p 3/2')
ax1[0].plot(bindingEn,counts_Si0_1_2-background,'--',c=color,label='Si 2p 1/2')
color = next(ax1[0]._get_lines.prop_cycler)['color']
ax1[0].plot(bindingEn,counts_Si1_3_2-background,c=color,label='Si$^{1+}$ 2p 3/2')
ax1[0].plot(bindingEn,counts_Si1_1_2-background,'--',c=color,label='Si$^{1+}$ 2p 1/2')
color = next(ax1[0]._get_lines.prop_cycler)['color']
ax1[0].plot(bindingEn,counts_Si3_3_2-background,c=color,label='Si$^{3+}$ 2p 3/2')
ax1[0].plot(bindingEn,counts_Si3_1_2-background,'--',c=color,label='Si$^{3+}$ 2p 1/2')
color = next(ax1[0]._get_lines.prop_cycler)['color']
ax1[0].plot(bindingEn,counts_Si4_3_2-background,c=color,label='SiO$_2$ 2p 3/2')
ax1[0].plot(bindingEn,counts_Si4_1_2-background,'--',c=color,label='SiO$_2$ 2p 1/2')
color = next(ax1[0]._get_lines.prop_cycler)['color']
ax1[0].plot(bindingEn,counts_Si0_3_2+counts_Si0_1_2+counts_Si1_3_2+counts_Si1_1_2+counts_Si3_3_2+counts_Si3_1_2+counts_Si4_3_2+counts_Si4_1_2-8*background,c=color,label='Total Fit')
color = next(ax1[0]._get_lines.prop_cycler)['color']
ax1[0].plot(bindingEn,background,':',c=color,label='background')
ax1[0].plot(bindingEn,counts_Si0_3_2+counts_Si0_1_2+counts_Si1_3_2+counts_Si1_1_2+counts_Si3_3_2+counts_Si3_1_2+counts_Si4_3_2+counts_Si4_1_2-7*background,'--',c=color,label='Total Fit + bg')
ax1[0].legend()
ax1[0].grid()
ax1[0].set_ylabel('Arbitrary Units')
ax1[1].set_xlabel('Binding Energy (eV)')

ax1[1].plot(bindingEn,residuals,'-')
ax1[1].set_ylabel('Norm. Res.')
ax1[1].grid()

fig0.savefig('data_init.pdf',dpi=300)
fig1.savefig('fits.pdf',dpi=300)
plt.show()