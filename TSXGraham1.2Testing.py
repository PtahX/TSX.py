import time
import urllib.request
import urllib.error
import urllib.parse
import bs4
import requests
from bs4 import BeautifulSoup as soup
from bs4 import BeautifulSoup
from urllib.request import urlopen
import sys
import math
from math import sqrt
import decimal
import re

tickerTST = ['MFI.TO', 'POW.TO']

tsxFull = ['AAA.TO', 'AAB.TO', 'AAR-UN.TO', 'AAV.TO', 'ABK-A.TO', 'ABK-PR-C.TO', 'ABT.TO', 'ABX.TO', 'AC.TO', 'ACC.TO',
           'ACD.TO', 'ACO-X.TO', 'ACO-Y.TO', 'ACQ.TO', 'ACR-UN.TO', 'ACZ-UN.TO', 'AD.TO', 'ADC-UN.TO', 'ADN.TO',
           'ADV.TO', 'ADW-A.TO', 'ADW-B.TO', 'AEI.TO', 'AEM.TO', 'AET-DB.TO', 'AET-DB-A.TO', 'AET-UN.TO', 'AEU-UN.TO',
           'AEZ.TO', 'AF.TO', 'AFN.TO', 'AFN-DB-A.TO', 'AFN-DB-B.TO', 'AFN-R.TO', 'AGF-B.TO', 'AGI.TO', 'AGI-WT.TO',
           'AGT.TO', 'AGU.TO', 'AHF.TO', 'AHF-DB.TO', 'AHY-UN.TO', 'AI.TO', 'AI-DB.TO', 'AI-DB-A.TO', 'AI-DB-B.TO',
           'AIF.TO', 'AIF-DB-A.TO', 'AIM.TO', 'AIM-PR-A.TO', 'AIM-PR-C.TO', 'AJX.TO', 'AKG.TO', 'AKT-A.TO', 'AKT-B.TO',
           'ALA.TO', 'ALA-PR-A.TO', 'ALA-PR-E.TO', 'ALA-PR-G.TO', 'ALA-PR-U.TO', 'ALB.TO', 'ALB-PR-B.TO', 'ALC.TO',
           'ALC-DB.TO', 'ALS.TO', 'AM.TO', 'AMF.TO', 'AMM.TO', 'ANS.TO', 'ANV.TO', 'ANX.TO', 'AOG-UN.TO', 'AOI.TO',
           'AP-UN.TO', 'APS.TO', 'APY.TO', 'AQA.TO', 'AQN.TO', 'AQN-PR-A.TO', 'AQN-PR-D.TO', 'AR.TO', 'ARE.TO',
           'ARE-DB-A.TO', 'ARE-DB-B.TO', 'ARF.TO', 'ARF-DB.TO', 'ARG.TO', 'ARL.TO', 'ARX.TO', 'ASR.TO', 'ATA.TO',
           'ATD-A.TO', 'ATD-B.TO', 'ATH.TO', 'ATL.TO', 'ATN.TO', 'ATP.TO', 'ATP-DB-A.TO', 'ATP-DB-B.TO', 'ATP-DB-D.TO',
           'ATP-DB-U.TO', 'AUE.TO', 'AUF-UN.TO', 'AUI-UN.TO', 'AUM.TO', 'AUP.TO', 'AUQ.TO', 'AUZ-UN.TO', 'AV-UN.TO',
           'AVK.TO', 'AVL.TO', 'AVO.TO', 'AVP.TO', 'AW-UN.TO', 'AX-DB-F.TO', 'AX-DB-U.TO', 'AX-PR-A.TO', 'AX-PR-E.TO',
           'AX-PR-G.TO', 'AX-PR-U.TO', 'AX-UN.TO', 'AXF.TO', 'AXL.TO', 'AXL-DB.TO', 'AXL-DB-B.TO', 'AXR.TO', 'AXX.TO',
           'AXY.TO', 'AYA.TO', 'AYA-DB-A.TO', 'AYA-WT.TO', 'AYA-WT-A.TO', 'AZP-PR-A.TO', 'AZP-PR-B.TO', 'AZP-PR-C.TO',
           'AZZ.TO', 'BAA.TO', 'BAB-UN.TO', 'BAD.TO', 'BAM-A.TO', 'BAM-PF-A.TO', 'BAM-PF-B.TO', 'BAM-PF-C.TO',
           'BAM-PF-D.TO', 'BAM-PF-E.TO', 'BAM-PF-F.TO', 'BAM-PF-G.TO', 'BAM-PR-B.TO', 'BAM-PR-C.TO', 'BAM-PR-E.TO',
           'BAM-PR-G.TO', 'BAM-PR-K.TO', 'BAM-PR-M.TO', 'BAM-PR-N.TO', 'BAM-PR-R.TO', 'BAM-PR-T.TO', 'BAM-PR-X.TO',
           'BAM-PR-Z.TO', 'BAN.TO', 'BAR.TO', 'BB.TO', 'BBD-A.TO', 'BBD-B.TO', 'BBD-PR-B.TO', 'BBD-PR-C.TO',
           'BBD-PR-D.TO', 'BBL-A.TO', 'BBO.TO', 'BBO-PR-A.TO', 'BCB.TO', 'BCE.TO', 'BCE-PR-A.TO', 'BCE-PR-B.TO',
           'BCE-PR-C.TO', 'BCE-PR-D.TO', 'BCE-PR-E.TO', 'BCE-PR-F.TO', 'BCE-PR-G.TO', 'BCE-PR-H.TO', 'BCE-PR-I.TO',
           'BCE-PR-J.TO', 'BCE-PR-K.TO', 'BCE-PR-M.TO', 'BCE-PR-O.TO', 'BCE-PR-Q.TO', 'BCE-PR-R.TO', 'BCE-PR-S.TO',
           'BCE-PR-T.TO', 'BCE-PR-Y.TO', 'BCE-PR-Z.TO', 'BCI.TO', 'BDI.TO', 'BDT.TO', 'BEI-UN.TO', 'BEK-B.TO',
           'BEP-UN.TO', 'BGI-UN.TO', 'BHY-UN.TO', 'BI-UN.TO', 'BIG-D.TO', 'BIG-PR-D.TO', 'BIN.TO', 'BIP-UN.TO',
           'BIR.TO', 'BIR-PR-A.TO', 'BIR-PR-C.TO', 'BK.TO', 'BK-PR-A.TO', 'BKI.TO', 'BKL.TO', 'BKX.TO', 'BLB-UN.TO',
           'BLD.TO', 'BLU.TO', 'BLX.TO', 'BLX-DB.TO', 'BMO.TO', 'BMO-PR-J.TO', 'BMO-PR-K.TO', 'BMO-PR-L.TO',
           'BMO-PR-M.TO', 'BMO-PR-P.TO', 'BMO-PR-Q.TO', 'BMO-PR-R.TO', 'BMO-PR-S.TO', 'BMO-PR-T.TO', 'BMO-PR-W.TO',
           'BNE.TO', 'BNG.TO', 'BNK.TO', 'BNP.TO', 'BNS.TO', 'BNS-PR-A.TO', 'BNS-PR-B.TO', 'BNS-PR-C.TO',
           'BNS-PR-L.TO', 'BNS-PR-M.TO', 'BNS-PR-N.TO', 'BNS-PR-O.TO', 'BNS-PR-P.TO', 'BNS-PR-Q.TO', 'BNS-PR-R.TO',
           'BNS-PR-Y.TO', 'BNS-PR-Z.TO', 'BOS.TO', 'BOX-UN.TO', 'BOY.TO', 'BOY-DB-A.TO', 'BPF-UN.TO', 'BPO-PR-A.TO',
           'BPO-PR-H.TO', 'BPO-PR-J.TO', 'BPO-PR-K.TO', 'BPO-PR-N.TO', 'BPO-PR-P.TO', 'BPO-PR-R.TO', 'BPO-PR-T.TO',
           'BPO-PR-U.TO', 'BPO-PR-W.TO', 'BPO-PR-X.TO', 'BPO-PR-Y.TO', 'BPS-PR-A.TO', 'BPS-PR-B.TO', 'BPS-PR-C.TO',
           'BPS-PR-U.TO', 'BPY-UN.TO', 'BQE.TO', 'BR.TO', 'BRB.TO', 'BRE.TO', 'BRF-PR-A.TO', 'BRF-PR-C.TO',
           'BRF-PR-E.TO', 'BRF-PR-F.TO', 'BRP.TO', 'BRY.TO', 'BSC.TO', 'BSC-PR-B.TO', 'BSD-PR-A.TO', 'BSD-UN.TO',
           'BSE-UN.TO', 'BSO-UN.TO', 'BSX.TO', 'BTB-DB-C.TO', 'BTB-DB-D.TO', 'BTB-DB-E.TO', 'BTB-UN.TO', 'BTE.TO',
           'BTO.TO', 'BU.TO', 'BUA-UN.TO', 'BUF.TO', 'BUI.TO', 'BX.TO', 'BXE.TO', 'BXF.TO', 'BXS-DB-B.TO', 'BYD-DB.TO',
           'BYD-DB-A.TO', 'BYD-UN.TO', 'BYL.TO', 'CAE.TO', 'CAG-UN.TO', 'CAH-UN.TO', 'CAL.TO', 'CAM.TO', 'CAM-DB.TO',
           'CAR-UN.TO', 'CAS.TO', 'CAX.TO', 'CAZ.TO', 'CBD.TO', 'CBD-A.TO', 'CBF.TO', 'CBH.TO', 'CBH-A.TO', 'CBL.TO',
           'CBN.TO', 'CBN-A.TO', 'CBO.TO', 'CBO-A.TO', 'CBQ.TO', 'CBQ-A.TO', 'CBR.TO', 'CBR-A.TO', 'CBU.TO',
           'CBU-PR-A.TO', 'CCA.TO', 'CCI-UN.TO', 'CCL-A.TO', 'CCL-B.TO', 'CCM.TO', 'CCO.TO', 'CCS-PR-C.TO', 'CCT.TO',
           'CCV.TO', 'CCZ.TO', 'CDD-UN.TO', 'CDG.TO', 'CDH.TO', 'CDI.TO', 'CDU.TO', 'CDV.TO', 'CDZ.TO', 'CDZ-A.TO',
           'CED.TO', 'CEE.TO', 'CEF-A.TO', 'CEF-U.TO', 'CES.TO', 'CES-A.TO', 'CES-B.TO', 'CET.TO', 'CEU.TO', 'CEW.TO',
           'CEW-A.TO', 'CF.TO', 'CF-PR-A.TO', 'CF-PR-C.TO', 'CFF.TO', 'CFN.TO', 'CFP.TO', 'CFW.TO', 'CFX.TO', 'CG.TO',
           'CGG.TO', 'CGI.TO', 'CGI-PR-C.TO', 'CGI-PR-D.TO', 'CGJ.TO', 'CGL.TO', 'CGL-C.TO', 'CGO.TO', 'CGR.TO',
           'CGR-A.TO', 'CGX.TO', 'CGX-DB-A.TO', 'CHB.TO', 'CHB-A.TO', 'CHE-DB.TO', 'CHE-DB-A.TO', 'CHE-DB-B.TO',
           'CHE-UN.TO', 'CHH.TO', 'CHH-NT.TO', 'CHI.TO', 'CHI-A.TO', 'CHL.TO', 'CHP-UN.TO', 'CHR-A.TO', 'CHR-B.TO',
           'CHW.TO', 'CHW-DB.TO', 'CIA.TO', 'CIC.TO', 'CIE.TO', 'CIE-A.TO', 'CIF.TO', 'CIF-A.TO', 'CIQ-UN.TO',
           'CIU-PR-A.TO', 'CIU-PR-C.TO', 'CIX.TO', 'CJ.TO', 'CJP.TO', 'CJP-A.TO', 'CJR-B.TO', 'CJT.TO', 'CJT-A.TO',
           'CJT-DB-A.TO', 'CJT-DB-B.TO', 'CKE.TO', 'CKI.TO', 'CLF.TO', 'CLF-A.TO', 'CLG.TO', 'CLL.TO', 'CLO.TO',
           'CLO-A.TO', 'CLR.TO', 'CLS.TO', 'CLU.TO', 'CLU-A.TO', 'CLU-B.TO', 'CLU-C.TO', 'CM.TO', 'CM-PR-E.TO',
           'CM-PR-G.TO', 'CM-PR-O.TO', 'CM-PR-P.TO', 'CMG.TO', 'CMH.TO', 'CML.TO', 'CMR.TO', 'CMW.TO', 'CMW-A.TO',
           'CMZ-UN.TO', 'CNE.TO', 'CNE-DB.TO', 'CNL.TO', 'CNQ.TO', 'CNR.TO', 'CNU.TO', 'COM.TO', 'COP.TO', 'COS.TO',
           'COW.TO', 'COW-A.TO', 'COX-UN.TO', 'CP.TO', 'CPD.TO', 'CPD-A.TO', 'CPF-UN.TO', 'CPG.TO', 'CPH.TO', 'CPI.TO',
           'CPN.TO', 'CPT.TO', 'CPW-DB.TO', 'CPX.TO', 'CPX-PR-A.TO', 'CPX-PR-C.TO', 'CPX-PR-E.TO', 'CQE.TO', 'CR.TO',
           'CRG.TO', 'CRH.TO', 'CRJ.TO', 'CRK.TO', 'CRK-WT.TO', 'CRP.TO', 'CRQ.TO', 'CRQ-A.TO', 'CRR-DB-C.TO',
           'CRR-DB-D.TO', 'CRR-DB-E.TO', 'CRR-UN.TO', 'CRT-UN.TO', 'CS.TO', 'CSB-UN.TO', 'CSD.TO', 'CSD-A.TO', 'CSE.TO',
           'CSE-DB-A.TO', 'CSE-PR-A.TO', 'CSH-DB-B.TO', 'CSH-UN.TO', 'CSU.TO', 'CSU-DB.TO', 'CSW-A.TO', 'CSW-B.TO',
           'CSY.TO', 'CTC.TO', 'CTC-A.TO', 'CTF-UN.TO', 'CTH.TO', 'CTU-A.TO', 'CTY.TO', 'CU.TO', 'CU-PR-C.TO',
           'CU-PR-D.TO', 'CU-PR-E.TO', 'CU-PR-F.TO', 'CU-PR-G.TO', 'CU-X.TO', 'CUD.TO', 'CUD-A.TO', 'CUF-DB-D.TO',
           'CUF-DB-E.TO', 'CUF-UN.TO', 'CUM.TO', 'CUP-U.TO', 'CUR.TO', 'CUS.TO', 'CUS-DB-A.TO', 'CUS-DB-B.TO',
           'CUS-DB-C.TO', 'CUS-DB-D.TO', 'CVD.TO', 'CVD-A.TO', 'CVE.TO', 'CVG.TO', 'CVI-A.TO', 'CVL.TO', 'CVL-DB.TO',
           'CWB.TO', 'CWB-PR-B.TO', 'CWF.TO', 'CWI.TO', 'CWL.TO', 'CWO.TO', 'CWO-A.TO', 'CWT-DB-B.TO', 'CWT-UN.TO',
           'CWW.TO', 'CWW-A.TO', 'CWX.TO', 'CWX-DB.TO', 'CXA-B.TO', 'CXF.TO', 'CXF-A.TO', 'CXI.TO', 'CXN.TO', 'CXR.TO',
           'CXS.TO', 'CYB.TO', 'CYH.TO', 'CYH-A.TO', 'CYT.TO', 'CZN.TO', 'CZQ.TO', 'D-DB-H.TO', 'D-UN.TO', 'DA-A.TO',
           'DA-DB-A.TO', 'DA-RT-A.TO', 'DBO.TO', 'DC-A.TO', 'DC-DB.TO', 'DC-PR-B.TO', 'DC-PR-C.TO', 'DC-PR-D.TO',
           'DCD-UN.TO', 'DCF.TO', 'DCF-DB.TO', 'DCI.TO', 'DDC.TO', 'DEE.TO', 'DEJ.TO', 'DEN.TO', 'DF.TO', 'DF-PR-A.TO',
           'DFN.TO', 'DFN-PR-A.TO', 'DGC.TO', 'DGI.TO', 'DGI-DB-A.TO', 'DGS.TO', 'DGS-PR-A.TO', 'DH.TO', 'DH-DB.TO',
           'DHX-A.TO', 'DHX-B.TO', 'DII-A.TO', 'DII-B.TO', 'DII-DB-U.TO', 'DIN-DB.TO', 'DIR-DB.TO', 'DIR-UN.TO',
           'DIV.TO', 'DL.TO', 'DLR.TO', 'DLR-U.TO', 'DML.TO', 'DMM.TO', 'DNA.TO', 'DNA-WT.TO', 'DNA-WT-A.TO', 'DNG.TO',
           'DNT.TO', 'DOL.TO', 'DOM-UN.TO', 'DOO.TO', 'DPM.TO', 'DPM-WT-A.TO', 'DR.TO', 'DR-DB-A.TO', 'DRA-UN.TO',
           'DRG-DB.TO', 'DRG-UN.TO', 'DRM.TO', 'DRM-PR-A.TO', 'DRN.TO', 'DRT.TO', 'DRX.TO', 'DS.TO', 'DSG.TO',
           'DSL-UN.TO', 'DTX.TO', 'DW.TO', 'DWI.TO', 'DWI-WT.TO', 'DXM.TO', 'DXM-A.TO', 'E.TO', 'E-WT.TO', 'EB-UN.TO',
           'EBC-UN.TO', 'EBF-UN.TO', 'EBT-UN.TO', 'ECA.TO', 'ECF-UN.TO', 'ECI.TO', 'ECI-DB.TO', 'ECO.TO', 'ECP.TO',
           'EDR.TO', 'EDT.TO', 'EDV.TO', 'EE.TO', 'EE-DB.TO', 'EFH.TO', 'EFL.TO', 'EFN.TO', 'EFN-DB.TO', 'EFN-PR-A.TO',
           'EFN-PR-C.TO', 'EFN-PR-E.TO', 'EFR.TO', 'EFR-DB.TO', 'EFX.TO', 'EGL-UN.TO', 'EGZ.TO', 'EH.TO', 'EIF.TO',
           'EIF-DB-C.TO', 'EIF-DB-D.TO', 'EIF-DB-E.TO', 'EIF-DB-F.TO', 'EIF-DB-G.TO', 'EIT-UN.TO', 'ELA-UN.TO',
           'ELB-UN.TO', 'ELD.TO', 'ELF.TO', 'ELF-PR-F.TO', 'ELF-PR-G.TO', 'ELF-PR-H.TO', 'ELR.TO', 'ELV.TO', 'EMA.TO',
           'EMA-PR-A.TO', 'EMA-PR-C.TO', 'EMA-PR-E.TO', 'EMA-PR-F.TO', 'EMD.TO', 'EMP-A.TO', 'ENB.TO', 'ENB-PF-A.TO',
           'ENB-PF-C.TO', 'ENB-PF-E.TO', 'ENB-PF-G.TO', 'ENB-PF-U.TO', 'ENB-PF-V.TO', 'ENB-PR-A.TO', 'ENB-PR-B.TO',
           'ENB-PR-D.TO', 'ENB-PR-F.TO', 'ENB-PR-H.TO', 'ENB-PR-J.TO', 'ENB-PR-N.TO', 'ENB-PR-P.TO', 'ENB-PR-T.TO',
           'ENB-PR-U.TO', 'ENB-PR-V.TO', 'ENB-PR-Y.TO', 'ENF.TO', 'ENI-UN.TO', 'ENL.TO', 'ENT.TO', 'ENT-DB.TO',
           'EOM.TO', 'EPS.TO', 'EPS-DB.TO', 'EQ.TO', 'EQB.TO', 'EQB-PR-C.TO', 'EQI.TO', 'EQU-DB-B.TO', 'ER.TO',
           'ERD.TO', 'ERF.TO', 'ERM.TO', 'ESI.TO', 'ESL.TO', 'ESN.TO', 'ESP.TO', 'ET.TO', 'ETG.TO', 'ETP.TO',
           'ETP-A.TO', 'ETX.TO', 'EUR.TO', 'EUR-A.TO', 'EVT.TO', 'EXE.TO', 'EXE-DB-B.TO', 'EXF.TO', 'EXM.TO', 'EXN.TO',
           'F-UN.TO', 'F-WT.TO', 'FAI.TO', 'FAO.TO', 'FAO-U.TO', 'FAP.TO', 'FAR.TO', 'FBS-B.TO', 'FBS-PR-C.TO', 'FC.TO',
           'FC-DB-A.TO', 'FC-DB-B.TO', 'FC-DB-C.TO', 'FC-DB-D.TO', 'FCO.TO', 'FCR.TO', 'FCR-DB-D.TO', 'FCR-DB-E.TO',
           'FCR-DB-F.TO', 'FCR-DB-G.TO', 'FCR-DB-H.TO', 'FCR-DB-I.TO', 'FCR-DB-J.TO', 'FCS-PR-C.TO', 'FCS-UN.TO',
           'FCU.TO', 'FDE.TO', 'FDE-A.TO', 'FDS-UN.TO', 'FDV.TO', 'FDV-A.TO', 'FDY.TO', 'FDY-A.TO', 'FER.TO', 'FFH.TO',
           'FFH-PR-C.TO', 'FFH-PR-D.TO', 'FFH-PR-E.TO', 'FFH-PR-G.TO', 'FFH-PR-I.TO', 'FFH-PR-K.TO', 'FFH-U.TO',
           'FFI-UN.TO', 'FFN.TO', 'FFN-PR-A.TO', 'FGX.TO', 'FHB.TO', 'FHB-A.TO', 'FHC.TO', 'FHD.TO', 'FHE.TO', 'FHG.TO',
           'FHH.TO', 'FHQ.TO', 'FHU.TO', 'FHY.TO', 'FIC.TO', 'FIE.TO', 'FIE-A.TO', 'FIH-U.TO', 'FLI.TO', 'FLI-A.TO',
           'FM.TO', 'FN.TO', 'FN-PR-A.TO', 'FNI.TO', 'FNM-UN.TO', 'FNV.TO', 'FNV-WT-A.TO', 'FOR.TO', 'FOS.TO', 'FP.TO',
           'FPX.TO', 'FR.TO', 'FRC.TO', 'FRF.TO', 'FRL-UN.TO', 'FRO.TO', 'FRU.TO', 'FRX.TO', 'FRX-WT.TO', 'FSD-UN.TO',
           'FSL.TO', 'FSL-A.TO', 'FSV.TO', 'FSY.TO', 'FSZ.TO', 'FT.TO', 'FTG.TO', 'FTN.TO', 'FTN-PR-A.TO', 'FTP.TO',
           'FTP-DB.TO', 'FTP-DB-A.TO', 'FTS.TO', 'FTS-PR-E.TO', 'FTS-PR-F.TO', 'FTS-PR-G.TO', 'FTS-PR-H.TO',
           'FTS-PR-J.TO', 'FTS-PR-K.TO', 'FTS-PR-M.TO', 'FTT.TO', 'FTU.TO', 'FTU-PR-B.TO', 'FUD.TO', 'FUD-A.TO',
           'FVI.TO', 'FVL.TO', 'FXF.TO', 'FXF-A.TO', 'FXM.TO', 'FXM-A.TO', 'G.TO', 'GBT-A.TO', 'GBU.TO', 'GC.TO',
           'GCG.TO', 'GCG-A.TO', 'GCL.TO', 'GCL-DB-A.TO', 'GCM.TO', 'GCM-NT-U.TO', 'GCM-WT.TO', 'GCM-WT-A.TO',
           'GCS-PR-A.TO', 'GCT.TO', 'GCT-C.TO', 'GDC.TO', 'GDG-UN.TO', 'GDL.TO', 'GDP-UN.TO', 'GDS.TO', 'GEI.TO',
           'GEN.TO', 'GEO.TO', 'GGA.TO', 'GGD.TO', 'GGT-UN.TO', 'GH.TO', 'GH-DB.TO', 'GHC-UN.TO', 'GIB-A.TO',
           'GIF-UN.TO', 'GII-UN.TO', 'GIL.TO', 'GIX.TO', 'GLG.TO', 'GLN.TO', 'GMM-U.TO', 'GMO.TO', 'GMP.TO',
           'GMP-PR-B.TO', 'GMX.TO', 'GPF-UN.TO', 'GPR.TO', 'GQM.TO', 'GRT-UN.TO', 'GS.TO', 'GSB-UN.TO', 'GSC.TO',
           'GTE.TO', 'GTH.TO', 'GTU-U.TO', 'GTU-UN.TO', 'GTX.TO', 'GUD.TO', 'GUY.TO', 'GVC.TO', 'GWO.TO', 'GWO-PR-F.TO',
           'GWO-PR-G.TO', 'GWO-PR-H.TO', 'GWO-PR-I.TO', 'GWO-PR-L.TO', 'GWO-PR-M.TO', 'GWO-PR-N.TO', 'GWO-PR-P.TO',
           'GWO-PR-Q.TO', 'GWO-PR-R.TO', 'GWO-PR-S.TO', 'GWR.TO', 'GXE.TO', 'GXI.TO', 'GXI-DB.TO', 'GZT.TO', 'HAA.TO',
           'HAA-A.TO', 'HAB.TO', 'HAB-A.TO', 'HAC.TO', 'HAC-A.TO', 'HAD.TO', 'HAD-A.TO', 'HAF.TO', 'HAJ.TO', 'HAJ-A.TO',
           'HAL.TO', 'HAL-A.TO', 'HAU.TO', 'HAY-UN.TO', 'HAZ.TO', 'HAZ-A.TO', 'HBB.TO', 'HBC.TO', 'HBD.TO', 'HBF-UN.TO',
           'HBL-UN.TO', 'HBM.TO', 'HBM-WT.TO', 'HBP.TO', 'HBR.TO', 'HBU.TO', 'HCG.TO', 'HCI.TO', 'HDX.TO', 'HE.TO',
           'HE-RT.TO', 'HEA.TO', 'HEA-A.TO', 'HEA-U.TO', 'HEA-V.TO', 'HED.TO', 'HEE.TO', 'HEE-A.TO', 'HEF.TO',
           'HEF-A.TO', 'HEJ.TO', 'HEJ-A.TO', 'HEN-UN.TO', 'HEP.TO', 'HEP-A.TO', 'HER.TO', 'HEU.TO', 'HEW.TO', 'HEX.TO',
           'HEX-A.TO', 'HFD.TO', 'HFP.TO', 'HFP-A.TO', 'HFR.TO', 'HFR-A.TO', 'HFU.TO', 'HGD.TO', 'HGI-UN.TO', 'HGN.TO',
           'HGU.TO', 'HGY.TO', 'HGY-A.TO', 'HHF.TO', 'HHF-A.TO', 'HHL-UN.TO', 'HHY-UN.TO', 'HII.TO', 'HIU.TO', 'HIX.TO',
           'HJD.TO', 'HJU.TO', 'HLC.TO', 'HLC-DB.TO', 'HLC-DB-A.TO', 'HLF.TO', 'HMD.TO', 'HMF.TO', 'HMF-A.TO',
           'HMM-A.TO', 'HMU.TO', 'HND.TO', 'HNL.TO', 'HNU.TO', 'HNY.TO', 'HNY-A.TO', 'HNZ-A.TO', 'HNZ-B.TO', 'HOD.TO',
           'HOG.TO', 'HOT-UN.TO', 'HOU.TO', 'HPD.TO', 'HPF-UN.TO', 'HPR.TO', 'HPR-A.TO', 'HPS-A.TO', 'HPU.TO', 'HQD.TO',
           'HQU.TO', 'HR-DB-D.TO', 'HR-DB-E.TO', 'HR-DB-H.TO', 'HR-UN.TO', 'HRR-UN.TO', 'HRT.TO', 'HRX.TO',
           'HSB-PR-C.TO', 'HSB-PR-D.TO', 'HSC-UN.TO', 'HSD.TO', 'HSE.TO', 'HSE-PR-A.TO', 'HSE-PR-C.TO', 'HSL.TO',
           'HSL-A.TO', 'HSU.TO', 'HTD.TO', 'HUC.TO', 'HUF.TO', 'HUF-U.TO', 'HUG.TO', 'HUN.TO', 'HUS-U.TO', 'HUS-V.TO',
           'HUT.TO', 'HUT-A.TO', 'HUV.TO', 'HUZ.TO', 'HVI.TO', 'HVU.TO', 'HWD.TO', 'HWO.TO', 'HXD.TO', 'HXE.TO',
           'HXF.TO', 'HXS.TO', 'HXS-U.TO', 'HXT.TO', 'HXT-U.TO', 'HXU.TO', 'HYB-UN.TO', 'HYD.TO', 'HYG.TO', 'HYI.TO',
           'HYI-A.TO', 'HZD.TO', 'HZM.TO', 'HZU.TO', 'I.TO', 'IAE.TO', 'IAG.TO', 'IAG-PR-A.TO', 'IAG-PR-F.TO',
           'IAG-PR-G.TO', 'IAM.TO', 'IBG.TO', 'IBG-DB.TO', 'IBG-DB-A.TO', 'IBG-DB-B.TO', 'IBG-DB-C.TO', 'ICE.TO',
           'ICP.TO', 'IDC.TO', 'IDE-UN.TO', 'IDG.TO', 'IDM.TO', 'IDR-UN.TO', 'IDX-UN.TO', 'IE.TO', 'IE-DB.TO',
           'IFB-UN.TO', 'IFC.TO', 'IFC-PR-A.TO', 'IFC-PR-C.TO', 'IFL-UN.TO', 'IFP.TO', 'IFP-R.TO', 'IGM.TO',
           'IGM-PR-B.TO', 'IGT.TO', 'IHL-UN.TO', 'III.TO', 'IIP-UN.TO', 'ILV.TO', 'IM.TO', 'IMG.TO', 'IMO.TO', 'IMP.TO',
           'IMV.TO', 'INC-UN.TO', 'INE.TO', 'INE-DB.TO', 'INE-PR-A.TO', 'INE-PR-C.TO', 'INN-DB-D.TO', 'INN-DB-E.TO',
           'INN-DB-F.TO', 'INN-DB-G.TO', 'INN-UN.TO', 'INO-UN.TO', 'INQ.TO', 'INV.TO', 'IPL.TO', 'IRD.TO', 'IRG.TO',
           'IRG-WT.TO', 'IRL.TO', 'ISL-U.TO', 'ISL-UN.TO', 'ISM.TO', 'ISV.TO', 'IT.TO', 'IT-DB.TO', 'IT-DB-A.TO',
           'ITC.TO', 'ITH.TO', 'ITP.TO', 'IVN.TO', 'IVN-WT.TO', 'IVW.TO', 'IXR.TO', 'JDN.TO', 'JE.TO', 'JE-DB.TO',
           'JE-DB-B.TO', 'JEC.TO', 'JFS-UN.TO', 'JOY.TO', 'K.TO', 'KAT.TO', 'KBL.TO', 'KDX.TO', 'KEG-UN.TO', 'KEL.TO',
           'KER.TO', 'KEY.TO', 'KFS.TO', 'KFS-WT-V.TO', 'KGI.TO', 'KGI-DB.TO', 'KGI-DB-A.TO', 'KLS.TO', 'KMP.TO',
           'KMP-DB-A.TO', 'KMP-DB-B.TO', 'KOR.TO', 'KPT.TO', 'KRN.TO', 'KSP-UN.TO', 'KWH-UN.TO', 'KXF.TO', 'KXS.TO',
           'L.TO', 'L-PR-A.TO', 'LAC.TO', 'LAM.TO', 'LAS-A.TO', 'LB.TO', 'LB-PR-F.TO', 'LB-PR-H.TO', 'LBS.TO',
           'LBS-PR-A.TO', 'LCS.TO', 'LCS-PR-A.TO', 'LEG.TO', 'LEX.TO', 'LFE.TO', 'LFE-PR-B.TO', 'LGC.TO', 'LGT-A.TO',
           'LGT-B.TO', 'LIF.TO', 'LII.TO', 'LIM.TO', 'LIQ.TO', 'LIQ-DB-A.TO', 'LMP.TO', 'LN.TO', 'LNF.TO', 'LNR.TO',
           'LOW-UN.TO', 'LPK.TO', 'LRE.TO', 'LRE-DB.TO', 'LRT-DB-G.TO', 'LRT-NT-A.TO', 'LRT-UN.TO', 'LRT-WT-A.TO',
           'LSA.TO', 'LSG.TO', 'LSG-DB.TO', 'LTS.TO', 'LUC.TO', 'LUG.TO', 'LUN.TO', 'LVN.TO', 'LVU-UN.TO', 'LW.TO',
           'LW-DB.TO', 'LWP.TO', 'LXF.TO', 'LXF-A.TO', 'LYD.TO', 'MA.TO', 'MAA.TO', 'MAG.TO', 'MAK.TO', 'MAL.TO',
           'MAQ.TO', 'MAR.TO', 'MAW.TO', 'MAX.TO', 'MAY.TO', 'MBA.TO', 'MBB-UN.TO', 'MBC.TO', 'MBC-WT.TO', 'MBK-UN.TO',
           'MBN.TO', 'MBT.TO', 'MBX.TO', 'MCB.TO', 'MCZ.TO', 'MDA.TO', 'MDF.TO', 'MDI.TO', 'MDN.TO', 'MDW.TO',
           'MDZ-A.TO', 'ME.TO', 'MEG.TO', 'MEQ.TO', 'MET.TO', 'MFC.TO', 'MFC-PR-A.TO', 'MFC-PR-B.TO', 'MFC-PR-C.TO',
           'MFC-PR-F.TO', 'MFC-PR-G.TO', 'MFC-PR-H.TO', 'MFC-PR-I.TO', 'MFC-PR-J.TO', 'MFC-PR-K.TO', 'MFC-PR-L.TO',
           'MFC-PR-M.TO', 'MFC-PR-N.TO', 'MFC-R.TO', 'MFI.TO', 'MFR-UN.TO', 'MG.TO', 'MGA.TO', 'MGO.TO', 'MGT.TO',
           'MHY-UN.TO', 'MIC.TO', 'MID-UN.TO', 'MIF-UN.TO', 'MIG-UN.TO', 'MKP.TO', 'MKZ-UN.TO', 'MLD-UN.TO',
           'MLE-UN.TO', 'MLF-UN.TO', 'MLP.TO', 'MM.TO', 'MM-DB-U.TO', 'MMF-UN.TO', 'MMM.TO', 'MMP-UN.TO', 'MMS.TO',
           'MMT.TO', 'MND.TO', 'MNS.TO', 'MNS-U.TO', 'MNT.TO', 'MNT-U.TO', 'MNW.TO', 'MOZ.TO', 'MPC.TO', 'MPC-C.TO',
           'MPI.TO', 'MPV.TO', 'MPV-RT.TO', 'MQA-UN.TO', 'MQI-UN.TO', 'MR-DB.TO', 'MR-UN.TO', 'MRC.TO', 'MRD.TO',
           'MRE.TO', 'MRG-DB.TO', 'MRG-UN.TO', 'MRI-U.TO', 'MRN.TO', 'MRT-DB-A.TO', 'MRT-UN.TO', 'MRU.TO', 'MSI.TO',
           'MSI-DB.TO', 'MSL.TO', 'MST-UN.TO', 'MSV.TO', 'MTG.TO', 'MTL.TO', 'MTY.TO', 'MUX.TO', 'MWE.TO', 'MX.TO',
           'MXF.TO', 'MXF-A.TO', 'MXG.TO', 'NA.TO', 'NA-PR-M.TO', 'NA-PR-Q.TO', 'NA-PR-S.TO', 'NA-PR-W.TO', 'NAF-UN.TO',
           'NAL.TO', 'NBD.TO', 'NBZ.TO', 'NCC-A.TO', 'NCC-B.TO', 'NCD-UN.TO', 'NCF.TO', 'NCQ.TO', 'NCU.TO', 'NDM.TO',
           'NDQ.TO', 'NEW-A.TO', 'NEW-PR-D.TO', 'NFI.TO', 'NFI-DB-U.TO', 'NG.TO', 'NGD.TO', 'NGD-WT-A.TO', 'NGI-UN.TO',
           'NGQ.TO', 'NHC.TO', 'NI.TO', 'NIF-UN.TO', 'NII.TO', 'NKO.TO', 'NKO-NT.TO', 'NLN.TO', 'NML.TO', 'NOA.TO',
           'NPC.TO', 'NPF-UN.TO', 'NPI.TO', 'NPI-DB-B.TO', 'NPI-DB-C.TO', 'NPI-PR-A.TO', 'NPI-PR-C.TO', 'NPK.TO',
           'NPR-UN.TO', 'NPS.TO', 'NRE.TO', 'NRF-UN.TO', 'NRG.TO', 'NRI.TO', 'NSI-PR-D.TO', 'NSU.TO', 'NTB.TO',
           'NUS.TO', 'NUX.TO', 'NVA.TO', 'NVC.TO', 'NVR.TO', 'NWC.TO', 'NWH-DB.TO', 'NWH-UN.TO', 'NWI.TO', 'NXC.TO',
           'NXF.TO', 'NXF-A.TO', 'NXF-B.TO', 'NXF-D.TO', 'NXJ.TO', 'OBM.TO', 'OCS-UN.TO', 'OCV-UN.TO', 'OCX.TO',
           'ODI-UN.TO', 'OER.TO', 'OFR-UN.TO', 'OGC.TO', 'OGD.TO', 'OGF-UN.TO', 'OLY.TO', 'OMI.TO', 'OMN.TO', 'ONC.TO',
           'OPM.TO', 'OR.TO', 'ORA.TO', 'ORE.TO', 'ORL.TO', 'ORT.TO', 'ORT-DB.TO', 'ORV.TO', 'OSF-UN.TO', 'OSL-UN.TO',
           'OSP.TO', 'OSP-PR-A.TO', 'OSU.TO', 'OTC.TO', 'OUY-U.TO', 'OUY-UN.TO', 'OVI-A.TO', 'OVI-B.TO', 'OXC.TO',
           'OXF.TO', 'OXF-A.TO', 'P.TO', 'P-DB-U.TO', 'P-DB-V.TO', 'P-WT.TO', 'PAA.TO', 'PAR-DB.TO', 'PAR-DB-A.TO',
           'PAR-DB-B.TO', 'PAR-UN.TO', 'PBD.TO', 'PBH.TO', 'PBH-DB-A.TO', 'PBH-DB-B.TO', 'PBH-DB-C.TO', 'PBI.TO',
           'PBI-B.TO', 'PBL.TO', 'PBU-UN.TO', 'PBY-UN.TO', 'PCD-UN.TO', 'PCY.TO', 'PD.TO', 'PDC.TO', 'PDF.TO', 'PDL.TO',
           'PDL-DB.TO', 'PDN.TO', 'PDV.TO', 'PDV-PR-A.TO', 'PEG.TO', 'PEU.TO', 'PEU-B.TO', 'PEY.TO', 'PFB.TO',
           'PFD-U.TO', 'PFD-UN.TO', 'PFH.TO', 'PFL.TO', 'PFR-UN.TO', 'PG.TO', 'PGD.TO', 'PGD-WT.TO', 'PGF.TO',
           'PGF-DB-B.TO', 'PGI-UN.TO', 'PGL.TO', 'PHE.TO', 'PHE-B.TO', 'PHR.TO', 'PHS-U.TO', 'PHX.TO', 'PHY-U.TO',
           'PIC-A.TO', 'PIC-PR-A.TO', 'PIH.TO', 'PIN.TO', 'PJC-A.TO', 'PKI.TO', 'PKI-DB-A.TO', 'PLG.TO', 'PLI.TO',
           'PLS.TO', 'PLT-DB.TO', 'PLT-UN.TO', 'PLZ-DB-B.TO', 'PLZ-DB-C.TO', 'PLZ-DB-D.TO', 'PLZ-UN.TO', 'PMB-UN.TO',
           'PME.TO', 'PMM.TO', 'PMT.TO', 'PMT-DB-E.TO', 'PNC-A.TO', 'PNC-B.TO', 'PNC-RT.TO', 'PNP.TO', 'PNP-DB.TO',
           'POM.TO', 'POT.TO', 'POU.TO', 'POW.TO', 'POW-PR-A.TO', 'POW-PR-B.TO', 'POW-PR-C.TO', 'POW-PR-D.TO',
           'POW-PR-E.TO', 'POW-PR-F.TO', 'POW-PR-G.TO', 'PPL.TO', 'PPL-DB-C.TO', 'PPL-DB-E.TO', 'PPL-DB-F.TO',
           'PPL-PR-A.TO', 'PPL-PR-C.TO', 'PPL-PR-E.TO', 'PPL-PR-G.TO', 'PPS.TO', 'PPT-U.TO', 'PPY.TO', 'PRA.TO',
           'PRE.TO', 'PRF-UN.TO', 'PRK.TO', 'PRU.TO', 'PRW.TO', 'PSA.TO', 'PSB.TO', 'PSD.TO', 'PSF-UN.TO', 'PSG.TO',
           'PSI.TO', 'PSK.TO', 'PTB.TO', 'PTM.TO', 'PTS.TO', 'PUD.TO', 'PUD-B.TO', 'PUR.TO', 'PVG.TO', 'PVS-PR-A.TO',
           'PVS-PR-B.TO', 'PVS-PR-C.TO', 'PVS-PR-D.TO', 'PWB.TO', 'PWB-PR-A.TO', 'PWC.TO', 'PWC-NT-C.TO', 'PWC-PR-A.TO',
           'PWC-PR-B.TO', 'PWF.TO', 'PWF-PR-A.TO', 'PWF-PR-E.TO', 'PWF-PR-F.TO', 'PWF-PR-G.TO', 'PWF-PR-H.TO',
           'PWF-PR-I.TO', 'PWF-PR-K.TO', 'PWF-PR-L.TO', 'PWF-PR-O.TO', 'PWF-PR-P.TO', 'PWF-PR-R.TO', 'PWF-PR-S.TO',
           'PWF-PR-T.TO', 'PWT.TO', 'PXC.TO', 'PXF.TO', 'PXT.TO', 'PXU.TO', 'PXX.TO', 'PZA.TO', 'PZG.TO', 'QBR-A.TO',
           'QBR-B.TO', 'QEC.TO', 'QLT.TO', 'QQC.TO', 'QRM.TO', 'QRM-WT.TO', 'QSP-UN.TO', 'QSR.TO', 'QXM.TO', 'QXM-A.TO',
           'R.TO', 'RAV-UN.TO', 'RBA.TO', 'RBM.TO', 'RBN-UN.TO', 'RBO.TO', 'RBS.TO', 'RBS-PR-B.TO', 'RC.TO', 'RCD.TO',
           'RCH.TO', 'RCI-A.TO', 'RCI-B.TO', 'RCL.TO', 'RCO-UN.TO', 'RDI.TO', 'RDK.TO', 'RDL.TO', 'RE.TO', 'REF-UN.TO',
           'REI-PR-A.TO', 'REI-PR-C.TO', 'REI-UN.TO', 'REN.TO', 'RES.TO', 'RET.TO', 'RET-A.TO', 'RFP.TO', 'RGL.TO',
           'RGX.TO', 'RGX-DB.TO', 'RHI.TO', 'RHP.TO', 'RHU.TO', 'RIB-UN.TO', 'RIC.TO', 'RID.TO', 'RID-U.TO', 'RIO.TO',
           'RIT-UN.TO', 'RKN.TO', 'RLC.TO', 'RLC-DB.TO', 'RME.TO', 'RMM-DB-A.TO', 'RMM-DB-B.TO', 'RMM-DB-C.TO',
           'RMM-UN.TO', 'RMP.TO', 'RMX.TO', 'RMX-WT.TO', 'RN.TO', 'RNW.TO', 'RNX.TO', 'RNX-WT.TO', 'RON.TO',
           'RON-PR-A.TO', 'RPD.TO', 'RPD-U.TO', 'RPG.TO', 'RPI-UN.TO', 'RQC.TO', 'RQD.TO', 'RQE.TO', 'RQF.TO', 'RQG.TO',
           'RQH.TO', 'RQI.TO', 'RRF-UN.TO', 'RRX.TO', 'RSC.TO', 'RSI.TO', 'RSI-DB-C.TO', 'RSI-DB-D.TO', 'RTCM.TO',
           'RTG.TO', 'RTK.TO', 'RTRE.TO', 'RTU-UN.TO', 'RUD.TO', 'RUD-U.TO', 'RUS.TO', 'RUS-DB.TO', 'RVM.TO', 'RVX.TO',
           'RWC.TO', 'RWC-A.TO', 'RWE.TO', 'RWE-A.TO', 'RWE-B.TO', 'RWE-D.TO', 'RWU.TO', 'RWU-A.TO', 'RWU-B.TO',
           'RWU-D.TO', 'RWW.TO', 'RWW-A.TO', 'RWW-B.TO', 'RXD.TO', 'RXD-U.TO', 'RY.TO', 'RY-PR-A.TO', 'RY-PR-B.TO',
           'RY-PR-C.TO', 'RY-PR-D.TO', 'RY-PR-E.TO', 'RY-PR-F.TO', 'RY-PR-G.TO', 'RY-PR-H.TO', 'RY-PR-I.TO',
           'RY-PR-J.TO', 'RY-PR-K.TO', 'RY-PR-L.TO', 'RY-PR-W.TO', 'RY-PR-Z.TO', 'S.TO', 'SAM.TO', 'SAP.TO', 'SAS.TO',
           'SAU.TO', 'SBB.TO', 'SBC.TO', 'SBC-PR-A.TO', 'SBI.TO', 'SBN.TO', 'SBN-PR-A.TO', 'SBR.TO', 'SBT-U.TO',
           'SBT-UN.TO', 'SCC.TO', 'SCI-UN.TO', 'SCL.TO', 'SCP.TO', 'SCU.TO', 'SCW-UN.TO', 'SCY.TO', 'SDY.TO', 'SEA.TO',
           'SEC.TO', 'SEN.TO', 'SEQ.TO', 'SEQ-DB.TO', 'SES.TO', 'SFI-UN.TO', 'SGF.TO', 'SGL.TO', 'SGQ.TO', 'SGY.TO',
           'SIF-UN.TO', 'SII.TO', 'SIN-UN.TO', 'SIS.TO', 'SJ.TO', 'SJR-B.TO', 'SJR-PR-A.TO', 'SKG-UN.TO', 'SLF.TO',
           'SLF-PR-A.TO', 'SLF-PR-B.TO', 'SLF-PR-C.TO', 'SLF-PR-D.TO', 'SLF-PR-E.TO', 'SLF-PR-G.TO', 'SLF-PR-H.TO',
           'SLF-PR-I.TO', 'SLR.TO', 'SLW.TO', 'SMA.TO', 'SMC.TO', 'SMF.TO', 'SMT.TO', 'SMU-UN.TO', 'SNC.TO', 'SOX.TO',
           'SOX-DB.TO', 'SOX-DB-A.TO', 'SOY.TO', 'SPB.TO', 'SPB-DB-E.TO', 'SPB-DB-F.TO', 'SPB-DB-G.TO', 'SPB-DB-H.TO',
           'SPE.TO', 'SPM.TO', 'SPT.TO', 'SQP.TO', 'SQZ.TO', 'SRT-U.TO', 'SRT-UN.TO', 'SRV-UN.TO', 'SSF-UN.TO',
           'SSL.TO', 'SSL-WT-A.TO', 'SSL-WT-B.TO', 'SSO.TO', 'ST.TO', 'STB.TO', 'STB-DB-B.TO', 'STB-DB-C.TO',
           'STB-DB-U.TO', 'STN.TO', 'STNC.TO', 'STNU.TO', 'SU.TO', 'SUM.TO', 'SUO.TO', 'SVB.TO', 'SVC.TO', 'SVL.TO',
           'SVM.TO', 'SVR.TO', 'SVR-C.TO', 'SVY.TO', 'SW.TO', 'SWD.TO', 'SWH.TO', 'SWY.TO', 'SWY-WT-A.TO', 'SXI.TO',
           'SXP.TO', 'T.TO', 'TA.TO', 'TA-PR-D.TO', 'TA-PR-F.TO', 'TA-PR-H.TO', 'TA-PR-J.TO', 'TAO.TO', 'TBE.TO',
           'TBE-DB.TO', 'TBL.TO', 'TBL-NT.TO', 'TC.TO', 'TCK-A.TO', 'TCK-B.TO', 'TCL-A.TO', 'TCL-B.TO', 'TCM.TO',
           'TCN.TO', 'TCN-DB.TO', 'TCN-DB-A.TO', 'TCP.TO', 'TCS.TO', 'TCT-UN.TO', 'TCW.TO', 'TCZ.TO', 'TD.TO',
           'TD-PF-A.TO', 'TD-PF-B.TO', 'TD-PF-C.TO', 'TD-PR-P.TO', 'TD-PR-Q.TO', 'TD-PR-R.TO', 'TD-PR-S.TO',
           'TD-PR-T.TO', 'TD-PR-Y.TO', 'TD-PR-Z.TO', 'TDG.TO', 'TDS-C.TO', 'TDS-PR-C.TO', 'TEI.TO', 'TEI-DB.TO',
           'TEL.TO', 'TET.TO', 'TFI.TO', 'TGA-DB.TO', 'TGF-UN.TO', 'TGL.TO', 'TGL-DB.TO', 'TGO.TO', 'TGZ.TO', 'TH.TO',
           'THB.TO', 'THO.TO', 'TIH.TO', 'TKM.TO', 'TKO.TO', 'TLB.TO', 'TLF-UN.TO', 'TLM.TO', 'TLM-PR-A.TO', 'TLO.TO',
           'TLV.TO', 'TMA.TO', 'TMB.TO', 'TMC.TO', 'TMC-DB.TO', 'TMD.TO', 'TMD-WT.TO', 'TMD-WT-A.TO', 'TMD-WT-B.TO',
           'TMD-WT-C.TO', 'TMD-WT-D.TO', 'TMD-WT-E.TO', 'TMI.TO', 'TMI-B.TO', 'TML.TO', 'TMM.TO', 'TN-DB.TO',
           'TN-UN.TO', 'TNP.TO', 'TNT-UN.TO', 'TNX.TO', 'TOF-UN.TO', 'TOG.TO', 'TOOC.TO', 'TOS.TO', 'TOT.TO',
           'TOT-DB.TO', 'TOU.TO', 'TPH.TO', 'TPH-DB-C.TO', 'TPH-DB-D.TO', 'TPH-DB-E.TO', 'TPH-DB-F.TO', 'TPK.TO',
           'TPL.TO', 'TPX-A.TO', 'TPX-B.TO', 'TR.TO', 'TRF-UN.TO', 'TRH-UN.TO', 'TRI.TO', 'TRI-PR-B.TO', 'TRL.TO',
           'TRP.TO', 'TRP-PR-A.TO', 'TRP-PR-B.TO', 'TRP-PR-C.TO', 'TRP-PR-D.TO', 'TRP-PR-E.TO', 'TRP-PR-F.TO', 'TRQ.TO',
           'TRY.TO', 'TRZ-A.TO', 'TRZ-B.TO', 'TS-B.TO', 'TSL.TO', 'TST.TO', 'TT.TO', 'TTCD.TO', 'TTCS.TO', 'TTE-UN.TO',
           'TTEN.TO', 'TTFS.TO', 'TTGD.TO', 'TTH.TO', 'TTHC.TO', 'TTIN.TO', 'TTMN.TO', 'TTMT.TO', 'TTRE.TO', 'TTTK.TO',
           'TTTS.TO', 'TTUT.TO', 'TTY-UN.TO', 'TUT-UN.TO', 'TV.TO', 'TVA-B.TO', 'TVA-RT.TO', 'TVI.TO', 'TVK.TO',
           'TWC.TO', 'TX.TO', 'TX-DB-B.TO', 'TXBA.TO', 'TXBB.TO', 'TXBE.TO', 'TXBM.TO', 'TXCE.TO', 'TXCT.TO', 'TXCX.TO',
           'TXDC.TO', 'TXDE.TO', 'TXDV.TO', 'TXEI.TO', 'TXEW.TO', 'TXF.TO', 'TXF-A.TO', 'TXFO.TO', 'TXG.TO', 'TXGE.TO',
           'TXGM.TO', 'TXHB.TO', 'TXHE.TO', 'TXHU.TO', 'TXIE.TO', 'TXL.TO', 'TXLV.TO', 'TXOE.TO', 'TXP.TO', 'TXPL.TO',
           'TXPR.TO', 'TXSC.TO', 'TXSI.TO', 'TXSX.TO', 'TXSY.TO', 'TXT-PR-A.TO', 'TXT-UN.TO', 'TXTW.TO', 'TZS.TO',
           'TZZ.TO', 'U.TO', 'UCD-UN.TO', 'UEX.TO', 'UFS.TO', 'UHB.TO', 'ULV.TO', 'UNC.TO', 'UNG-PR-C.TO',
           'UNG-PR-D.TO', 'UNS.TO', 'UNS-DB.TO', 'UR.TO', 'URB.TO', 'URB-A.TO', 'URE.TO', 'URZ.TO', 'USB.TO',
           'USB-U.TO', 'USF-UN.TO', 'USH-UN.TO', 'USM-UN.TO', 'UST-PR-B.TO', 'UST-UN.TO', 'UTC-C.TO', 'UTE-UN.TO',
           'UUU-DB-A.TO', 'UWE.TO', 'UXM.TO', 'UXM-A.TO', 'UXM-B.TO', 'UXM-D.TO', 'VA.TO', 'VAB.TO', 'VBG.TO', 'VBU.TO',
           'VCE.TO', 'VCM.TO', 'VCN.TO', 'VDU.TO', 'VDY.TO', 'VE.TO', 'VEE.TO', 'VEF.TO', 'VEM.TO', 'VET.TO', 'VFF.TO',
           'VFV.TO', 'VGG.TO', 'VGH.TO', 'VGI-UN.TO', 'VGQ.TO', 'VGZ.TO', 'VIC.TO', 'VIC-DB.TO', 'VIC-DB-A.TO',
           'VII.TO', 'VIP-UN.TO', 'VIXC.TO', 'VLE.TO', 'VLN.TO', 'VNP.TO', 'VNP-DB.TO', 'VNR.TO', 'VNR-PR-A.TO',
           'VRE.TO', 'VRX.TO', 'VSB.TO', 'VSC.TO', 'VSN.TO', 'VSN-PR-A.TO', 'VSN-PR-C.TO', 'VSP.TO', 'VUN.TO', 'VUS.TO',
           'VXC.TO', 'VXM.TO', 'VXM-A.TO', 'VXM-B.TO', 'VXM-D.TO', 'VXS.TO', 'VXSC.TO', 'W-PR-H.TO', 'W-PR-J.TO',
           'WB.TO', 'WCM-A.TO', 'WCM-B.TO', 'WCP.TO', 'WDN.TO', 'WDO.TO', 'WEF.TO', 'WEQ.TO', 'WEQ-DB.TO',
           'WEQ-DB-C.TO', 'WEW.TO', 'WFC.TO', 'WFS.TO', 'WFS-PR-A.TO', 'WFT.TO', 'WG.TO', 'WIN.TO', 'WIR-U.TO',
           'WJA.TO', 'WJA-A.TO', 'WJX.TO', 'WLC.TO', 'WM.TO', 'WN.TO', 'WN-PR-A.TO', 'WN-PR-C.TO', 'WN-PR-D.TO',
           'WN-PR-E.TO', 'WPK.TO', 'WPT.TO', 'WPX.TO', 'WRG.TO', 'WRN.TO', 'WS.TO', 'WSP.TO', 'WTE.TO', 'WXM.TO',
           'WXM-A.TO', 'X.TO', 'XAL.TO', 'XAW.TO', 'XBB.TO', 'XBM.TO', 'XBZ.TO', 'XCB.TO', 'XCD.TO', 'XCG.TO', 'XCH.TO',
           'XCR.TO', 'XCS.TO', 'XCV.TO', 'XDC.TO', 'XDV.TO', 'XEB.TO', 'XEC.TO', 'XEF.TO', 'XEG.TO', 'XEH.TO', 'XEI.TO',
           'XEM.TO', 'XEN.TO', 'XEU.TO', 'XFH.TO', 'XFN.TO', 'XFR.TO', 'XGB.TO', 'XGC.TO', 'XGD.TO', 'XGI.TO', 'XGR.TO',
           'XHB.TO', 'XHC.TO', 'XHD.TO', 'XHG.TO', 'XHM-A.TO', 'XHU.TO', 'XHY.TO', 'XIC.TO', 'XID.TO', 'XIG.TO',
           'XIN.TO', 'XIT.TO', 'XIU.TO', 'XLA.TO', 'XLB.TO', 'XMA.TO', 'XMD.TO', 'XMF-A.TO', 'XMF-PR-B.TO',
           'XMF-PR-C.TO', 'XMI.TO', 'XMM.TO', 'XMU.TO', 'XMV.TO', 'XMW.TO', 'XPF.TO', 'XQB.TO', 'XQB-A.TO', 'XQQ.TO',
           'XRB.TO', 'XRC.TO', 'XRE.TO', 'XRG.TO', 'XSB.TO', 'XSH.TO', 'XSI.TO', 'XSP.TO', 'XSQ.TO', 'XSR.TO', 'XST.TO',
           'XSU.TO', 'XTC.TO', 'XTD.TO', 'XTD-PR-A.TO', 'XTG.TO', 'XTR.TO', 'XUH.TO', 'XUS.TO', 'XUT.TO', 'XUU.TO',
           'XVX.TO', 'XWD.TO', 'XXM.TO', 'XXM-A.TO', 'XXM-B.TO', 'XXM-D.TO', 'XYM.TO', 'Y.TO', 'Y-WT.TO', 'YCM.TO',
           'YCM-PR-A.TO', 'YCM-PR-B.TO', 'YGR.TO', 'YMI.TO', 'YOU-UN.TO', 'YP-UN.TO', 'YPG-DB.TO', 'YRB-A.TO', 'YRI.TO',
           'YXM.TO', 'YXM-A.TO', 'YXM-B.TO', 'YXM-D.TO', 'ZAG.TO', 'ZAR.TO', 'ZAR-DB.TO', 'ZAZ.TO', 'ZBK.TO', 'ZCH.TO',
           'ZCL.TO', 'ZCM.TO', 'ZCN.TO', 'ZCS.TO', 'ZDB.TO', 'ZDI.TO', 'ZDJ.TO', 'ZDM.TO', 'ZDV.TO', 'ZDY.TO',
           'ZDY-U.TO', 'ZEA.TO', 'ZEB.TO', 'ZEF.TO', 'ZEL.TO', 'ZEM.TO', 'ZEO.TO', 'ZEQ.TO', 'ZFH.TO', 'ZFL.TO',
           'ZFM.TO', 'ZFS.TO', 'ZGD.TO', 'ZGI.TO', 'ZGQ.TO', 'ZHY.TO', 'ZIC.TO', 'ZIC-U.TO', 'ZID.TO', 'ZIN.TO',
           'ZJG.TO', 'ZJN.TO', 'ZJO.TO', 'ZLB.TO', 'ZLC.TO', 'ZLU.TO', 'ZLU-U.TO', 'ZMI.TO', 'ZMP.TO', 'ZMT.TO',
           'ZMU.TO', 'ZNC.TO', 'ZPL.TO', 'ZPR.TO', 'ZPS.TO', 'ZQQ.TO', 'ZRE.TO', 'ZRR.TO', 'ZSP.TO', 'ZSP-U.TO',
           'ZST.TO', 'ZSU.TO', 'ZUB.TO', 'ZUD.TO', 'ZUE.TO', 'ZUH.TO', 'ZUQ.TO', 'ZUT.TO', 'ZWA.TO', 'ZWB.TO', 'ZWH.TO',
           'ZWH-U.TO', 'ZWU.TO', 'ZXB.TO', 'ZXC.TO', 'ZXD.TO', 'ZXM.TO', 'ZXM-A.TO', 'ZXM-B.TO']

tsx500 = ['CP.TO', 'ATD-B.TO', 'PPL.TO', 'CNR.TO', 'GET.TO', 'IPL.TO', 'MG.TO', 'CNQ.TO', 'SAP.TO', 'BAM-A.TO', 'CM.TO',
          'TRP.TO',
          'ECA.TO', 'ENB.TO', 'BMO.TO', 'TD.TO', 'NA.TO', 'VRX.TO', 'FM.TO', 'RY.TO', 'SLF.TO', 'MFC.TO', 'BNS.TO',
          'IMO.TO', 'L.TO', 'T.TO', 'FFH.TO', 'SJR-B.TO', 'TRI.TO', 'POT.TO', 'TOU.TO', 'CPG.TO', 'CU.TO', 'SU.TO',
          'BCE.TO', 'GIB-A.TO', 'HSE.TO', 'PWF.TO', 'AGU.TO', 'COS.TO', 'POW.TO', 'GWO.TO', 'CVE.TO', 'IGM.TO',
          'RCI-B.TO', 'WN.TO', 'G.TO', 'ABX.TO', 'TLM.TO', 'CCT.TO', 'TCK-B.TO', 'AYA.TO', 'AC-A.TO', 'PXT.TO',
          'RRX.TO', 'ACQ.TO', 'SES.TO', 'LNR.TO', 'SCC.TO', 'POU.TO', 'GC.TO', 'KEY.TO', 'BIR.TO', 'OTC.TO', 'CEU.TO',
          'VSN.TO', 'TOG.TO', 'GEI.TO', 'CCL-B.TO', 'CSU.TO', 'WCP.TO', 'KEL.TO', 'FSV.TO', 'PSI.TO', 'BNK.TO',
          'FTT.TO', 'HCG.TO', 'MFI.TO', 'MX.TO', 'ALA.TO', 'AQN.TO', 'NVA.TO', 'STN.TO', 'ENF.TO', 'EFX.TO', 'WSP.TO',
          'SPB.TO', 'THO.TO', 'AEM.TO', 'FNV.TO', 'HBM.TO', 'RUS.TO', 'SCL.TO', 'CPX.TO', 'MRC.TO', 'SGY.TO', 'CWB.TO',
          'TFI.TO', 'SNC.TO', 'PJC-A.TO', 'WJA.TO', 'RON.TO', 'MIC.TO', 'WPK.TO', 'DH.TO', 'GIL.TO', 'WFT.TO', 'NPI.TO',
          'CTC-A.TO', 'PAA.TO', 'ERF.TO', 'CCA.TO', 'FN.TO', 'BEI-UN.TO', 'LUN.TO', 'RBA.TO', 'AX-UN.TO', 'BNE.TO',
          'OCX.TO', 'ELF.TO', 'BPY-UN.TO', 'PKI.TO', 'IFC.TO', 'PEY.TO', 'RNW.TO', 'EMA.TO', 'PD.TO', 'REF-UN.TO',
          'QBR-B.TO', 'CAR-UN.TO', 'VET.TO', 'CAE.TO', 'TIH.TO', 'ARX.TO', 'CSH-UN.TO', 'SJ.TO', 'WTE.TO', 'DOL.TO',
          'GRT-UN.TO', 'X.TO', 'FTS.TO', 'ELD.TO', 'CFP.TO', 'BOX-UN.TO', 'AP-UN.TO', 'BTE.TO', 'IAG.TO', 'REI-UN.TO',
          'LB.TO', 'HR-UN.TO', 'FCR.TO', 'PGF.TO', 'CFW.TO', 'TXG.TO', 'CHP-UN.TO', 'CWT-UN.TO', 'BIN.TO', 'FRU.TO',
          'MRU.TO', 'BB.TO', 'CIX.TO', 'CUF-UN.TO', 'MTL.TO', 'CRR-UN.TO', 'LEG.TO', 'BNP.TO', 'EFN.TO', 'AIM.TO',
          'CGX.TO', 'ACO-X.TO', 'NGD.TO', 'HBC.TO', 'MEG.TO', 'IMX.TO', 'MDA.TO', 'TRQ.TO', 'DGC.TO', 'CLS.TO',
          'SLW.TO', 'BXE.TO', 'CCO.TO', 'D-UN.TO', 'TET.TO', 'CG.TO', 'EMP-A.TO', 'CJR-B.TO', 'BRP.TO', 'TCW.TO',
          'MBT.TO', 'DOO.TO', 'BTO.TO', 'TA.TO', 'LIF.TO', 'ATH.TO', 'ESI.TO', 'AOI.TO', 'YRI.TO', 'K.TO', 'BBD-B.TO',
          'IMG.TO', 'PWT.TO', 'PGF.TO', 'CFW.TO', 'TXG.TO', 'CHP-UN.TO', 'CWT-UN.TO', 'BIN.TO', 'FRU.TO', 'MRU.TO',
          'BB.TO', 'CIX.TO', 'CUF-UN.TO', 'MTL.TO', 'CRR-UN.TO', 'LEG.TO', 'BNP.TO', 'EFN.TO', 'AIM.TO', 'CGX.TO',
          'ACO-X.TO', 'NGD.TO', 'HBC.TO', 'MEG.TO', 'IMX.TO', 'MDA.TO', 'TRQ.TO', 'DGC.TO', 'CLS.TO', 'SLW.TO',
          'BXE.TO', 'CCO.TO', 'D-UN.TO', 'TET.TO', 'CG.TO', 'EMP-A.TO', 'CJR-B.TO', 'BRP.TO', 'TCW.TO', 'MBT.TO',
          'DOO.TO', 'BTO.TO', 'TA.TO', 'LIF.TO', 'ATH.TO', 'ESI.TO', 'AOI.TO', 'YRI.TO', 'K.TO', 'BBD-B.TO', 'IMG.TO',
          'PWT.TO', 'ELW.TO', 'CXR.TO', 'PRC.TO', 'SPE.TO', 'TMD.TO', 'TKM.TO', 'RE.TO', 'PTK.TO', 'YGR.TO', 'TVE.TO',
          'LGT.A.TO', 'DHX.TO', 'DEE.TO', 'SW.TO', 'LSG.TO', 'PLI.TO', 'KLS.TO', 'LUC.TO', 'SMF.TO', 'CKE.TO', 'IT.TO',
          'BLD.TO', 'NVC.TO', 'MAL.TO', 'CHR.B.TO', 'CJT.TO', 'BCI.TO', 'CKI.TO', 'HWO.TO', 'RCL.TO', 'R.TO', 'HYG.TO',
          'AIF.TO', 'CF.TO', 'TTH.TO', 'AGT.TO', 'CSO.TO', 'PMT.TO', 'CLR.TO', 'EH.TO', 'TV.TO', 'WEF.TO', 'CR.TO',
          'PUR.TO', 'SYZ.TO', 'GUY.TO', 'XTC.TO', 'SRX.TO', 'BYD.UN.TO', 'GS.TO', 'PSG.TO', 'BOS.TO', 'PPY.TO',
          'PNE.TO', 'POM.TO', 'AAV.TO', 'ECI.TO', 'HLP.UN.TO', 'CUM.TO', 'WED.TO', 'NAL.TO', 'INN.UN.TO', 'SUM.TO',
          'SVC.TO', 'QLT.TO', 'VNP.TO', 'INP.TO', 'LGO.TO', 'RMP.TO', 'KGI.TO', 'MDZ.A.TO', 'WB.TO', 'SEC.TO', 'CNE.TO',
          'EQB.TO', 'RIO.TO', 'PLS.TO', 'GGD.TO', 'SOY.TO', 'Y.TO', 'ESL.TO', 'PHX.TO', 'LAS.A.TO', 'LW.TO', 'BCM.TO',
          'BAD.TO', 'VLN.TO', 'PBH.TO', 'IFP.TO', 'NG.TO', 'WIR.U.TO', 'MND.TO', 'MEQ.TO', 'GDC.TO', 'NOA.TO', 'MAG.TO',
          'KDX.TO', 'RLC.TO', 'EXE.TO', 'EPS.TO', 'TMA.TO', 'HRX.TO', 'CWC.TO', 'BLX.TO', 'CHE.UN.TO', 'MSI.TO',
          'BDT.TO', 'DSG.TO', 'NFI.TO', 'XDC.TO', 'TS.B.TO', 'FVI.TO', 'CSS.TO', 'GCG.A.TO', 'WIN.TO', 'TMB.TO',
          'AFN.TO', 'PRI.TO', 'NSU.TO', 'FRC.TO', 'DND.TO', 'INE.TO', 'AVO.TO', 'DRM.TO', 'VGQ.TO', 'RMC.TO',
          'MST.UN.TO', 'GH.TO', 'MKP.TO', 'HLF.TO', 'MRD.TO', 'GMP.TO', 'TOT.TO', 'MRT.UN.TO', 'TCN.TO', 'CQE.TO',
          'UNS.TO', 'DIR.UN.TO', 'PG.TO', 'FSZ.TO', 'EDR.TO', 'TGZ.TO', 'ZCL.TO', 'NUS.TO', 'AI.TO', 'CSE.TO', 'KBL.TO',
          'AW.UN.TO', 'ALS.TO', 'TWC.TO', 'MRG.UN.TO', 'ISV.TO', 'WRG.TO', 'MRE.TO', 'ET.TO', 'MVN.TO', 'GBT.A.TO',
          'P.TO', 'BDI.TO', 'NIF.UN.TO', 'TNP.TO', 'STB.TO', 'ALC.TO', 'PRB.TO', 'ADN.TO', 'CVG.TO', 'DR.TO',
          'ACR.UN.TO', 'FCU.TO', 'LNF.TO', 'GBU.TO', 'AKT.A.TO', 'ARE.TO', 'DDC.TO', 'WFC.TO', 'CAM.TO', 'AAR.UN.TO',
          'PZA.TO', 'CGO.TO', 'ATP.TO', 'CDI.TO', 'RCH.TO', 'TCL.A.TO', 'TVA.B.TO', 'NPR.UN.TO', 'DRG.UN.TO', 'FC.TO',
          'SSO.TO', 'CFX.TO', 'DML.TO', 'IIP.UN.TO', 'CS.TO', 'SII.TO', 'HOT.UN.TO', 'AUQ.TO', 'RMX.TO', 'WEQ.TO',
          'DTX.TO', 'TPH.TO', 'ADW.A.TO', 'NGQ.TO', 'WJX.TO', 'PLT.UN.TO', 'SCP.TO', 'VNR.TO', 'IDG.TO', 'ZAR.TO',
          'SOX.TO', 'NWC.TO', 'CAS.TO', 'PTA.TO', 'TKO.TO', 'BKX.TO', 'ABT.TO', 'QEC.TO', 'MMT.TO', 'AGF.B.TO',
          'CVL.TO', 'NWH.UN.TO', 'CSW.A.TO', 'PLZ.UN.TO', 'JE.TO', 'RMM.UN.TO', 'MPV.TO', 'MTY.TO', 'XSR.TO', 'KMP.TO',
          'PXX.TO', 'ESN.TO', 'BCB.TO', 'OER.TO', 'SVL.TO', 'ITP.TO', 'LRE.TO', 'S.TO', 'CMG.TO', 'RME.TO', 'DII.B.TO',
          'ATA.TO', 'BPF.UN.TO', 'MDI.TO', 'PTM.TO', 'AD.TO', 'DC.A.TO', 'TBE.TO', 'SSL.TO', 'SVY.TO', 'NCC.A.TO',
          'MDF.TO', 'CGG.TO', 'TGL.TO', 'HNZ.A.TO', 'NDQ.TO', 'VIC.TO', 'LIQ.TO', 'RTK.TO', 'KAT.TO', 'WZR.TO',
          'CDV.TO', 'TDG.TO', 'PVG.TO', 'AKG.TO', 'EXF.TO', 'DCI.TO', 'EIF.TO', 'HNL.TO', 'DPM.TO', 'CFN.TO', 'ACC.TO',
          'TMM.TO', 'TRZ.TO', 'RSI.TO', 'LII.TO', 'CNL.TO', 'NBD.TO', 'LTS.TO', 'SWY.TO', 'III.TO', 'SNM.TO',
          'RET.A.TO', 'TCM.TO', 'RKN.TO', 'SMT.TO', 'GLN.TO', 'PTS.TO', 'FR.TO', 'ASR.TO', 'OXC.TO', 'SMA.TO', 'CUS.TO',
          'SEA.TO', 'ANS.TO', 'TNX.TO', 'NTB.TO', 'AR.TO', 'HGN.TO', 'IVN.TO', 'AGI.TO', 'SVM.TO', 'WPT.TO']

############# Soup Calls for Yahoo!#########################

# from http://www.pythoncentral.io/python-beautiful-soup-example-yahoo-finance-scraper/

#############################################################################


# ************************************** STOCK PREREQUISITS TO MAKE SHORT LIST *******************************************************************************


def yahooKeyStats(stock):
    try:
        optionsUrl = "https://ca.finance.yahoo.com/q/ks?s=" + stock
        optionsPage = urlopen(optionsUrl)
        soup = BeautifulSoup(optionsPage)

        # Price to Book values
        tag7 = soup.findAll('td', {'class': 'yfnc_tablehead1'})[7]
        pbr = float(tag7.nextSibling.text)
        if float(pbr) < 1.5:

          # Price to Earnings
          tag3 = soup.findAll('td', {'class': 'yfnc_tablehead1'})[3]
          priceEarn = float(tag3.nextSibling.text)
          if (priceEarn * pbr) < 21:

            #Price to Earnings Growth
            tag5 = soup.findAll('td', {'class': 'yfnc_tablehead1'})[5]
            PEG = float(tag5.nextSibling.text)
            if 0 < float(PEG) < 1.0:

                # current ratio greater than 1.7
                tag27 = soup.findAll('td', {'class': 'yfnc_tablehead1'})[27]
                cRatio = float(tag27.nextSibling.text)
                if float(cRatio) > 1.9:

                    # debt to Equity Ratio
                    tag26 = soup.findAll('td', {'class': 'yfnc_tablehead1'})[26]
                    dToE = float(tag26.nextSibling.text)
                    if float(dToE) < 100:

                        # Price to Sales
                        tag5 = soup.findAll('td', {'class': 'yfnc_tablehead1'})[5]
                        priceSales = str(tag5.nextSibling.text)
                        if float(priceSales) < 1:

                            # *************************************** Graham Number Calculations *********************************************
                            print()
                            tag21 = soup.findAll('td', {'class': 'yfnc_tablehead1'})[21]
                            EPS = float(tag21.nextSibling.text)
                            #print(str(stock) + ('\n')+ ('\t') + ('EPS is') + ('\t') + str(EPS))

                            tag28 = soup.findAll('td', {'class': 'yfnc_tablehead1'})[28]
                            BPS = float(tag28.nextSibling.text)
                            #print(('\t') + ('BPS is') + ('\t') + str(BPS) + ('\n'))



                            print('##########################################')
                            priceTag = soup.findAll('span')[20]  #gets current stock price
                            currentPrice = float(priceTag.text)

                            grahamNum = float(math.sqrt(22.5 * EPS * BPS))
                            if currentPrice < grahamNum:
                                tag9 = soup.findAll('h2')[3]
                                fullname = str(tag9.text)
                                print(str(fullname))
                                print(stock)

                                print(('the Current Stock Price is:$') + ('\t') + str(currentPrice))
                                print('##########################################')
                                print()

                                #******************************** Screener Printouts *************************************
                                print('*')
                                print('The following elements pre-Screened to make the Short List')
                                print("\t" + ('Price to Book Ratio for') + "\t" + str(stock) + "\t" + str(pbr))
                                print(
                                    "\t" + ('Price to Earnings Ratio for') + "\t" + str(stock) + "\t" + str(priceEarn))
                                print("\t" + ('Price to Earnings Growth (PEG 5 year) between 0 and 1') + "\t" + str(
                                    stock) + "\t" + str(PEG))
                                print("\t" + ('Current Ratio greater than 1.9') + "\t" + str(stock) + "\t" + str(cRatio))
                                print("\t" + ('Debt to Equity Ratio is less than 100') + "\t" + str(stock) + "\t" + str(
                                    dToE))
                                print("\t" + ('price to Sales Ratio Less than 1') + "\t" + str(stock) + "\t" + str(
                                    priceSales))
                                #print("\t" +('Net Free Cash Flow is Greater than 0')  + "\t" +str(stock) + "\t" + str(netFreeCash))
                                print('*')

                                #************************************************************* VALUATION AND DIVIDENDS *****************************************************
                                print('VALUE FACTORS')

                                print(str(stock) + ('!!! TRADING BELOW GRAHAM NUMBER !!!'))

                                print(('Graham Number is: $') + ('\t') + str(grahamNum))

                                sellPrice = float(grahamNum * 1.5)
                                print(('Stock Sell Price is: $') + ('\t') + str(sellPrice))
                                print()

                                tag50 = soup.findAll('td', {'class': 'yfnc_tablehead1'})[50]
                                dividend = float(tag50.nextSibling.text)
                                print(('The Current Dividend is:') + ('\t') + str(dividend))

                                tag51 = soup.findAll('td', {'class': 'yfnc_tablehead1'})[51]
                                dividendYld = str(tag51.nextSibling.text)
                                print(('The Current Dividend Yield is:') + ('\t') + str(dividendYld))

                                tag52 = soup.findAll('td', {'class': 'yfnc_tablehead1'})[52]
                                fiveDividendYld = str(tag52.nextSibling.text)
                                print(('The 5 year average Dividend Yield is:') + ('\t') + str(fiveDividendYld))
                                print()

                                tag14 = soup.findAll('td', {'class': 'yfnc_tablehead1'})[14]
                                ROE = str(tag14.nextSibling.text)
                                print(('Return on Equity (Ideally over 20%):') + ('\t') + str(ROE))

                                print()
                                print()

                                #*****************************************************************GROWTH *********************************************************************
                                print('GROWTH FACTORS')

                                # Market Cap
                                tag0 = soup.findAll('td', {'class': 'yfnc_tablehead1'})[0]
                                mCap = str(tag0.nextSibling.text)
                                print(('The Market Cap (ideally is over $300 Million:)') + ('\t') + str(mCap))

                                # 17 Quarterly Revenue Growth
                                tag17 = soup.findAll('td', {'class': 'yfnc_tablehead1'})[17]
                                qEarn = str(tag17.nextSibling.text)
                                print(
                                    ('The Quarterly Revenue Growth (increased Sales over time):') + ('\t') + str(qEarn))


                                #43	% Held by Institutions1:N/A
                                tag43 = soup.findAll('td', {'class': 'yfnc_tablehead1'})[43]
                                institutions = str(tag43.nextSibling.text)
                                print(('Institutional Ownership (Ideally less than 60%):') + ('\t') + str(institutions))

                                #42	% Held by Insiders1:N/A
                                tag42 = soup.findAll('td', {'class': 'yfnc_tablehead1'})[42]
                                insiders = str(tag42.nextSibling.text)
                                print(('Insider Ownership:') + ('\t') + str(insiders))
                                print()
                                print()

                                #************************************************************************* CASH FLOWS************************************************************
                                print('CASH FLOWS')


                                # Price to Sales
                                tag5 = soup.findAll('td', {'class': 'yfnc_tablehead1'})[5]
                                priceSales = str(tag5.nextSibling.text)
                                print(('Price To Sales (The lower the better):') + ('\t') + str(priceSales))

                                # 12	Operating Margin (ttm):8.01% (AKA Net Profit Margin)


                                tag12 = soup.findAll('td', {'class': 'yfnc_tablehead1'})[12]
                                netProfit = str(tag12.nextSibling.text)
                                print(('Net Profit Margin (The higher the better):') + ('\t') + str(netProfit))


                                # 30 levered free cash flow
                                tag30 = soup.findAll('td', {'class': 'yfnc_tablehead1'})[30]
                                LFC = str(tag30.nextSibling.text)
                                print(('Net Free Cash Flow (Higher is better - No Negatives):') + ('\t') + str(LFC))


                                # 40 Shares Outstanding5:392.41M
                                tag40 = soup.findAll('td', {'class': 'yfnc_tablehead1'})[40]
                                Shares = str(tag40.nextSibling.text)
                                print(('Number of Shares Outstanding:') + ('\t') + str(Shares))
                                # ideally (FCF) / (# of shares) / (stock price) = Free Cash Yield goes here


                            #************************************************************************** TO ADD LATER ***************************************************************************


                            # also would like the average PE over 10 years
                            # EPS difference from previous year same quarter (eg 1st quarter 2013 vs 1st quarter 2014)



                            # Growth Factors
                            # IS EPS Growing at least 20% per year
                            # if EPS increases quarter after quater this is called earnings momentum


                            #print()
                            #print('##########################################')
                            #print()
                            #print()



    except Exception as e:
        sys.stdout.write("")

###########################################################
# Price to Book Ratio Function - This may need to go above the yahooKeyStats function?

print(
    'Version 1.0 of Stevens Toronto Stock Exchange Picker, checks the P/E, Book Value, PEG, Current Ratio, and Debt to Equity Ratio are all in range')

################### TICKER LOOPS
# tickerTST ## NYSE ## nasdaq ## amex ## tsx500 ## tsxFull


for eachStock in tsxFull:  # for every entity in the above this run yahookey stats
    yahooKeyStats(eachStock)
    time.sleep(2)

#############################

'''

0	Market Cap (intraday)5:992.79M
1	Enterprise Value (2015-01-26)3:1.06B
2	Trailing P/E (ttm, intraday):9.88
3	Forward P/E (fye 2015-12-31)1:9.04
4	PEG Ratio (5 yr expected)1:1.25
5	Price/Sales (ttm):0.94
6	Price/Book (mrq):2.39
7	Enterprise Value/Revenue (ttm)3:1.01
8	Enterprise Value/EBITDA (ttm)6:9.28
9	Fiscal Year Ends:Dec 31
10	Most Recent Quarter (mrq):2014-09-30
11	Profit Margin (ttm):10.07%
12	Operating Margin (ttm):8.01%
13	Return on Assets (ttm):7.88%
14	Return on Equity (ttm):28.29%
15	Revenue (ttm):1.05B
16	Revenue Per Share (ttm):2.67
17	Qtrly Revenue Growth (yoy):9.50%
18	Gross Profit (ttm):N/A
19	EBITDA (ttm)6:113.70M
20	Net Income Avl to Common (ttm):105.40M
21	Diluted EPS (ttm):0.26
22	Qtrly Earnings Growth (yoy):-84.30%
23	Total Cash (mrq):15.40M
24	Total Cash Per Share (mrq):0.04
25	Total Debt (mrq):78.00M
26	Total Debt/Equity (mrq):18.97
27	Current Ratio (mrq):2.48
28	Book Value Per Share (mrq):1.05
29	Operating Cash Flow (ttm):91.70M
30	Levered Free Cash Flow (ttm):32.30M
31	Beta:N/A
32	52-Week Change3:15.00%
33	S&P500 52-Week Change3:15.17%
34	52-Week High (2015-01-02)3:2.80
35	52-Week Low (2014-10-14)3:1.91
36	50-Day Moving Average3:2.49
37	200-Day Moving Average3:2.38
38	Avg Vol (3 month)3:1,538,400
39	Avg Vol (10 day)3:2,402,110
40	Shares Outstanding5:392.41M
41	Float:391.86M
42	% Held by Insiders1:N/A
43	% Held by Institutions1:N/A
44	Shares Short 3:N/A
45	Short Ratio 3:N/A
46	Short % of Float 3:N/A
47	Shares Short (prior month)3:N/A
48	Forward Annual Dividend Rate4:N/A
49	Forward Annual Dividend Yield4:N/A
50	Trailing Annual Dividend Yield3:0.06
51	Trailing Annual Dividend Yield3:2.40%
52	5 Year Average Dividend Yield4:N/A
53	Payout Ratio4:N/A
54	Dividend Date3:2014-12-19
55	Ex-Dividend Date4:N/A
56	Last Split Factor (new per old)2:N/A
57	Last Split Date3:N/A


# Levered Free Cash Flow 30
           tag30 = soup.findAll('td', {'class': 'yfnc_tablehead1'})[30]
           netFCF = re.findall('[\d.]+', tag30.nextSibling.text)[0] # removes percentage sign & NEGATIVE Number :/
           netFreeCash = float(netFCF)
           if netFreeCash > 0:

# Levered Free Cash Flow 30
           tag30 = soup.findAll('td', {'class': 'yfnc_tablehead1'})[30]
           netFCF = re.findall('[\d.]+', tag30.nextSibling.text)[0] # removes percentage sign & NEGATIVE Number :/
           netFreeCash = float(netFCF)
           if netFreeCash > 0:

'''
