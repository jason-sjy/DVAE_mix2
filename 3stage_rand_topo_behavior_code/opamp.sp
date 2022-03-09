.inc 'gm+.sp'
.inc 'gm-.sp'
.inc 'gm+_middle.sp'
.inc 'gm-_middle.sp'
.subckt opamp vp vn out vb1 vb2 vdd
X_vin_1 net_vinp net_vinn net_1 vb1 vdd gm+ wp=wp_in_1*1u wn=wn_in_1*1u wb=wb_in_1*1u
X_1_2 net_1 net_2 vb2 vdd gm-_middle wp=wp_1_2*1u wn=wn_1_2*1u
X_2_vo net_2 net_vo vb1 vdd gm+_middle wp=wp_2_out*1u wb=wb_2_out*1u
R_L net_vo 0 r=0.15meg
C_L net_vo 0 c=10n
X_vin_vin_2 net_vinp net_vinn net_vin_2 vb1 vdd gm+ wn=wn_vin_vin_2*1u wp=wp_vin_vin_2*1u wb=wb_vin_vin_2*1u
R_vin_2_2 net_vin_2 net_2 r=r_vin_2_2*1meg
X_vin_vin_vo net_vinp net_vinn net_vin_vo vb1 vdd gm- wn=wn_vin_vin_vo*1u wp=wp_vin_vin_vo*1u wb=wb_vin_vin_vo*1u
C_vin_vo_vo net_vin_vo net_vo c=c_vin_vo_vo*1p
X_vo_1 net_vo net_1 vb2 vdd gm-_middle wp=wp_vo_1*1u wn=wn_vo_1*1u
C_vo_1 net_vo net_1 c=c_vo_1*1p
R_1_0 net_1 0 r=r_1_0*1meg
C_1_0 net_1 0 c=c_1_0*1p
