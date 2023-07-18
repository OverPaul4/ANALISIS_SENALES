"""
Report:
This script generate a word report with the results of the analysis from the line analizer

Dilan Andres Valencia Aguilar 
Over paul Hernandez
universidad tecnologica de pereira 
2023
"""

#importing libraries
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from scritps.scritps_general.scripts_general import *
import numpy as np


def tabla_info_general(voltage, current, cost_p, cost_q, time):
    vrms = v_rms(voltage)
    irms = i_rms(current)
    result = power(voltage, current)
    p = result[0]
    q = result[1]
    d = result[2]
    s = result[3]
    fp = result[4]
    harmonics = result[5]
    vrms_harmonic = result[9]
    irms_harmonic = result[10]
    result2 = energy(p[3], q[3], cost_p, cost_q, time)

    THD_V_A = (np.sqrt(np.sum(np.array(vrms_harmonic[0][1:]) ** 2)) / vrms_harmonic[0][0]) * 100
    THD_V_B = (np.sqrt(np.sum(np.array(vrms_harmonic[1][1:]) ** 2)) / vrms_harmonic[1][0]) * 100
    THD_V_C = (np.sqrt(np.sum(np.array(vrms_harmonic[2][1:]) ** 2)) / vrms_harmonic[2][0]) * 100

    THD_I_A = (np.sqrt(np.sum(np.array(irms_harmonic[0][1:]) ** 2)) / irms_harmonic[0][0]) * 100
    THD_I_B = (np.sqrt(np.sum(np.array(irms_harmonic[1][1:]) ** 2)) / irms_harmonic[1][0]) * 100
    THD_I_C = (np.sqrt(np.sum(np.array(irms_harmonic[2][1:]) ** 2)) / irms_harmonic[2][0]) * 100

    salida = [[' ', 'Phase A', 'Phase B', 'Phase C', 'Total/Equivalent/Cost'],
              ['VRMS', '{} V'.format(vrms[0]), '{} V'.format(vrms[1]), '{} V'.format(vrms[2]), 'N.A'],
              ['IRMS', '{} A'.format(irms[0]), '{} V'.format(irms[1]), '{} V'.format(irms[2]), 'N.A'],
              ['P', '{} W'.format(p[0]), '{} W'.format(p[1]), '{} W'.format(p[2]), '{} W'.format(p[3])],
              ['Q', '{} VAR'.format(q[0]), '{} VAR'.format(q[1]), '{} VAR'.format(q[2]), '{} VAR'.format(q[3])],
              ['D', '{} VAD'.format(d[0]), '{} VAD'.format(d[1]), '{} VAD'.format(d[2]), '{} VAD'.format(d[3])],
              ['S', '{} VA'.format(s[0]), '{} VA'.format(s[1]), '{} VA'.format(s[2]), '{} VA'.format(s[3])],
              ['harmonics', '{}'.format(harmonics[0]), '{}'.format(harmonics[1]), '{}'.format(harmonics[2]), 'N.A'],
              ['THD_V', '{} %'.format(round(THD_V_A, 3)), '{} %'.format(round(THD_V_B, 3)), '{} %'.format(round(THD_V_C, 3)), 'N.A'],
              ['THD_I', '{} %'.format(round(THD_I_A, 3)), '{} %'.format(round(THD_I_B, 3)), '{} %'.format(round(THD_I_C, 3)), 'N.A'],
              ['fp', '{}'.format(fp[0]), '{}'.format(fp[1]), '{}'.format(fp[2]), '{}'.format(fp[3])],
              ['Ep', 'N.A', 'N.A', 'N.A', '{} kWh'.format(result2[0])],
              ['Eq', 'N.A', 'N.A', 'N.A', '{} kVARh'.format(result2[1])],
              ['$Ep', 'N.A', 'N.A', 'N.A', '$ {}'.format(result2[2])],
              ['$Eq', 'N.A', 'N.A', 'N.A', '$ {}'.format(result2[3])],
              ['$E', 'N.A', 'N.A', 'N.A', '$ {}'.format(result2[4])],
              ]
    
    return salida


    



#function to generate the report
def reporte(nodo, entrada1, voltage, current, cost_p, cost_q, time):
    if nodo == 'Node 1':
        nodo_s = 1
    elif nodo == 'Node 2':
        nodo_s = 2
    elif nodo == 'Node 3':
        nodo_s = 3

    #creating the pdf
    pdf=canvas.Canvas(f"Report_node{nodo_s}.pdf",pagesize=letter)

    #adding the title
    pdf.setFont("Times-Roman", 30)
    pdf.setFillColor(colors.black)
    pdf.drawString(120,750,f"Report from the line analizer: Node {nodo_s}")

    #adding the introduction
    pdf.setFont("Times-Roman", 15)
    introduccion= "in this report you will find the results of the analizer of lines, the results are the following:"
    pdf.drawString(30,700,introduccion)
    item1="1. signal trhee phase voltage per phase and per line "
    pdf.drawString(30,670,item1)
    item2="2. signal three phase current per line"
    pdf.drawString(30,630,item2)
    item3="3. phasorial diagram of the voltage and current per harmonics"
    pdf.drawString(30,590,item3)
    item4="4. Power triangle"
    pdf.drawString(30,550,item4)
    item5="5. Power Data"
    pdf.drawString(30,510,item5)
    item6="6. General information of the line"
    pdf.drawString(30,470,item6)

    #writing the results item 1
    pdf.setFont("Times-Roman", 20)
    pdf.drawString(30,420,"1. signal trhee phase voltage per phase and per line")
    pdf.setFont("Times-Roman", 15)
    Text1="Figures 1 and 2 show the results obtained from the measurements taken at the"
    pdf.drawString(30,390,Text1)
    Text2="input of the line, where the voltage per phase and per line is shown respectively."
    pdf.drawString(30,370,Text2)
    #adding the images
    #pdf.drawImage("voltage_per_phase.png", 30, 200, width=250, height=150)
    #pdf.drawImage("voltage_per_line.png", 300, 200, width=250, height=150)
    Figure1="Figure 1. Voltage per phase"
    pdf.drawString(50,180,Figure1)
    Figure2="Figure 2. Voltage per line"
    pdf.drawString(320,180,Figure2)

    #adding new page 
    pdf.showPage()

    #writing the results item 2
    pdf.setFont("Times-Roman", 20)
    pdf.drawString(30,750,"2. signal three phase current per line")
    pdf.setFont("Times-Roman", 15)
    Text3="Figures 3 and 4 show the results obtained from the measurements taken at the"
    pdf.drawString(30,710,Text3)
    Text4="input of the line, where the current per phase and per line is shown respectively."
    pdf.drawString(30,690,Text4)
    #adding the images
    #pdf.drawImage("current_per_phase.png", 30, 200, width=250, height=150)
    #pdf.drawImage("current_per_line.png", 300, 200, width=250, height=150)
    Figure3="Figure 3. Current per line or phase"
    pdf.drawString(180,600,Figure3)

    #writing the results item 3
    pdf.setFont("Times-Roman", 20)
    pdf.drawString(30,550,"3. phasorial diagram of the voltage and current per harmonics")
    pdf.setFont("Times-Roman", 15)
    Text5="The following figures depict the harmonic phasor diagrams taken from the samples"
    pdf.drawString(30,510,Text5)
    Text6="of the measuring system for the voltage and current signals."
    pdf.drawString(30,490,Text6)
    #adding the images
    #pdf.drawImage("voltage_harmonics.png", 30, 200, width=250, height=150)
    #pdf.drawImage("current_harmonics.png", 300, 200, width=250, height=150)
    Figure4="Figure 4. Phasorial diagrams of the voltage per harmonics"
    pdf.drawString(180,350,Figure4)
    Figure5="Figure 5. Phasorial diagrams of the current per harmonics"
    pdf.drawString(180,200,Figure5)

    #writing the results item 4
    pdf.setFont("Times-Roman", 20)
    pdf.drawString(30,150,"4. Power triangle")
    pdf.setFont("Times-Roman", 15)
    Text7="The following figure shows the power triangle of the line, where the active power,"
    pdf.drawString(30,110,Text7)
    Text8="reactive power and apparent power are shown per phase and the power triangle equilavent."
    pdf.drawString(30,90,Text8)
    Text9="with distortion power."
    pdf.drawString(30,70,Text9)
    #adding the images
    #pdf.drawImage("power_triangle.png", 30, 200, width=250, height=150)

    #adding new page
    pdf.showPage()
    pdf.setFont("Times-Roman", 15)
    Figure6="Figure 6. Power triangle per phase"
    pdf.drawString(180,650,Figure6)
    Figure7="Figure 7. Power triangle equilavent with distortion power"
    pdf.drawString(180,540,Figure7)

    #writing the results item 5
    pdf.setFont("Times-Roman", 20)
    pdf.drawString(30,450,"5. Power Data")
    pdf.setFont("Times-Roman", 15)
    Text10="The following table shows the power data of the line, where the active power,"
    pdf.drawString(30,410,Text10)
    Text11="reactive power and apparent power are shown per harmonics."
    pdf.drawString(30,390,Text11)
    
    #adding the table
    cabecera = ["Harmonic", "VRMS [V]", "IRMS [A]", "P [W]", "Q [VAR]","S [VA]", "fp"]
    data = entrada1[0]
    data.insert(0, cabecera)
 
    table=Table(data)
    table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                           ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                           ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                           ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                           ('FONTSIZE', (0, 0), (-1, 0), 12),
                           ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                           ('BACKGROUND', (0, 1), (-1, -1), colors.beige)]))
    table.wrapOn(pdf, 800, 600)
    table.drawOn(pdf, 130, 250)
    Text12="Table 1. Power data phase A"
    pdf.drawString(220,220,Text12)
    
    data2 = entrada1[1]
    data2.insert(0, cabecera)
    table=Table(data2)
    table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                           ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                           ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                           ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                           ('FONTSIZE', (0, 0), (-1, 0), 12),
                           ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                           ('BACKGROUND', (0, 1), (-1, -1), colors.beige)]))
    table.wrapOn(pdf, 800, 600)
    table.drawOn(pdf, 130, 60)
    Text13="Table 2. Power data phase B"
    pdf.drawString(220,40,Text13)

    #New page
    pdf.showPage()
    data3 = entrada1[2]
    data3.insert(0, cabecera)
    table=Table(data3)
    table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                            ('FONTSIZE', (0, 0), (-1, 0), 12),
                            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                            ('BACKGROUND', (0, 1), (-1, -1), colors.beige)]))
    table.wrapOn(pdf, 800, 600)
    table.drawOn(pdf, 130, 650)
    pdf.setFont("Times-Roman", 15)
    Text14="Table 3. Power data phase C"
    pdf.drawString(220,630,Text14)

    #writing the results item 6
    pdf.setFont("Times-Roman", 20)
    pdf.drawString(30,550,"6. General Results")
    pdf.setFont("Times-Roman", 15)
    Text15="The following table shows the general results of the line"
    pdf.drawString(30,510,Text15)
    #adding the table
    data4 = tabla_info_general(voltage, current, cost_p, cost_q, time)
    table=Table(data4)
    table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                            ('FONTSIZE', (0, 0), (-1, 0), 12),
                            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                            ('BACKGROUND', (0, 1), (-1, -1), colors.beige)]))
    table.wrapOn(pdf, 800, 600)
    table.drawOn(pdf, 130, 250)
    pdf.setFont("Times-Roman", 15)
    Text16="Table 4. General results"
    pdf.drawString(220,220,Text16)

    #adding new page
    pdf.showPage()
    #writing the considerations 
    pdf.setFont("Times-Roman", 20)
    pdf.drawString(230,150," Considerations")
    pdf.setFont("Times-Roman", 15)
    Text17="The following considerations were taken into account for the development of the project:"
    pdf.drawString(30,120,Text17)
    Text18="1. The line analizer detected harmonic in the network."
    pdf.drawString(30,100,Text18)
    Text19="2. The line analizer detected unbalance in the network."
    pdf.drawString(30,80,Text19)
    Text20="3. the network manager must take into account:"
    pdf.drawString(30,60,Text20)
    Text21="a. if THDi is less than 10% the network is at low risk of malfunctioning."
    pdf.drawString(50,40,Text21)
    Text22="b. if THDi is greater than 10% and less than 50% the network is at risk of"
    pdf.drawString(50,20,Text22)
    
    #adding new page
    # pdf.showPage()
    pdf.setFont("Times-Roman", 15)
    Text23="overheating of conductors and equipment."
    pdf.drawString(50,720,Text23)
    Text24="c. if THDi is greater than 50% the network has a high probability of dangerous"
    pdf.drawString(50,700,Text24)
    Text25="heating and gradation malfunctions."
    pdf.drawString(50,680,Text25)
    Text26="d. if THDv is less than 5% the network has a low risk of failure."
    pdf.drawString(50,660,Text26)
    Text27="e. if THDv is greater than 5% and less than 8% the network is at risk of overheating "
    pdf.drawString(50,640,Text27)
    Text28="and malfunctioning."
    pdf.drawString(50,620,Text28)
    Text29="f. if THDv is greater than 8% the network has a high risk of malfunctioning"
    pdf.drawString(50,600,Text29)
    Text30="4. The network has a problem of energy efficiency due to harmonics."
    pdf.drawString(30,580,Text30)
    Text31="5.the network can enter into resonance due to harmonics."
    pdf.drawString(30,560,Text31)

    #Writing the recommendations
    pdf.setFont("Times-Roman", 20)
    pdf.drawString(230,500," Recommendations")
    pdf.setFont("Times-Roman", 15)
    Text32="The following recommendations are made to the network manager:"
    pdf.drawString(30,470,Text32)
    Text33="1. The network manager must constantly analyze the line."
    pdf.drawString(30,450,Text33)
    Text34="2. The network manager must observe which electronic elements are harmonically."
    pdf.drawString(30,430,Text34)
    Text35="entering the network."
    pdf.drawString(30,410,Text35)
    Text36="3. A low-pass filter or a type c filter should be installed in case these electronic"
    pdf.drawString(30,390,Text36)
    Text37="elements are not detected and you still have harmonics in the network."
    pdf.drawString(30,370,Text37)
    Text38="4. Check if the system has non-linear loads and if so, disconnect them.."
    pdf.drawString(30,350,Text38)
    Text39="5. Comply with the network operator's regulations to avoid fines or legal problems."
    pdf.drawString(30,330,Text39)

    pdf.save()

# report=reporte()
# print("Report generated successfully")
