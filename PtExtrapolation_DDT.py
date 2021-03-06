from __future__ import print_function
from collections import OrderedDict
import ROOT
from math import sqrt
from array import array
import CMS_lumi
import tdrstyle

tdrstyle.setTDRStyle()
CMS_lumi.lumi_13TeV = ""
CMS_lumi.writeExtraText = 1
CMS_lumi.extraText = "Private Simulation"
CMS_lumi.lumi_sqrtS = "13 TeV"  # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)

iPos = 11
if(iPos == 0):
    CMS_lumi.relPosX = 0.12
iPeriod = 4


def getCanvas(title="c1"):
    H_ref = 600
    W_ref = 800
    W = W_ref
    H = H_ref

    T = 0.08 * H_ref
    B = 0.12 * H_ref
    L = 0.12 * W_ref
    R = 0.04 * W_ref

    c1 = ROOT.TCanvas(title, title, 50, 50, W, H)
    c1.SetFillColor(0)
    c1.SetBorderMode(0)
    c1.SetFrameFillStyle(0)
    c1.SetFrameBorderMode(0)
    c1.SetLeftMargin(L / W)
    c1.SetRightMargin(R / W)
    c1.SetTopMargin(T / H)
    c1.SetBottomMargin(B / H)
    c1.SetTickx(0)
    c1.SetTicky(0)
    c1.GetWindowHeight()
    c1.GetWindowWidth()
    c1.SetGrid()
    c1.cd()
    return c1


# masses = [600, 1000, 2000, 3000, 4000]

"""
Need the following infos for each working point and mass:
- eff Pythia HP
- eff Herwig HP
- eff Pythia LP
- eff Herwig LP
"""

eff_Dict_DDT = OrderedDict()
eff_Dict_DDT_unc = OrderedDict()


# eff_Dict_DDT[600] = (0.660980810235, 0.63829787234, 0.132196162047, 0.148936170213)
# eff_Dict_DDT_unc[600] = (0.0218584893822, 0.0700871339919, 0.0156398932799, 0.0519316628328)
# eff_Dict_DDT[1000] = (0.689706017879, 0.629590865842, 0.130126255645, 0.174881065652)
# eff_Dict_DDT_unc[1000] = (0.00444103097617, 0.00471051829788, 0.0032298004907, 0.00370534212707)
# eff_Dict_DDT[2000] = (0.649843804235, 0.585148514851, 0.155432141617, 0.195332390382)
# eff_Dict_DDT_unc[2000] = (0.00397446583098, 0.00414337912252, 0.00301877718404, 0.00333403909177)
# eff_Dict_DDT[3000] = (0.611562066917, 0.533394089311, 0.17362898436, 0.218461137873)
# eff_Dict_DDT_unc[3000] = (0.00395942185133, 0.00402508760369, 0.00307715476041, 0.00333379203328)
# eff_Dict_DDT[4000] = (0.600351339482, 0.521523178808, 0.18125352908, 0.230193769929)
# eff_Dict_DDT_unc[4000] = (0.00387981830324, 0.00391171232356, 0.00305131764753, 0.00329637902566)

# eff_Dict_DDT[600] = ( 0.230277185501, 0.255319148936, 0.626865671642, 0.574468085106)
# eff_Dict_DDT_unc[600] = ( 0.0194404455701, 0.0636030377173, 0.0223322985696, 0.0721190658978)
# eff_Dict_DDT[1000] = ( 0.218505206893, 0.178116079924, 0.639941019261, 0.65813510942)
# eff_Dict_DDT_unc[1000] = ( 0.00396697129467, 0.0037321186999, 0.00460810022673, 0.00462682871676)
# eff_Dict_DDT[2000] = ( 0.3216938563, 0.259335219236, 0.534189517529, 0.574257425743)
# eff_Dict_DDT_unc[2000] = ( 0.003892042979, 0.00368567377572, 0.00415619272894, 0.00415816909308)
# eff_Dict_DDT[3000] = ( 0.366990034977, 0.290456971748, 0.478453111595, 0.53033459185)
# eff_Dict_DDT_unc[3000] = ( 0.00391546275992, 0.00366274252562, 0.00405804687586, 0.00402666393282)
# eff_Dict_DDT[4000] = ( 0.411694585608, 0.330451312239, 0.438986134638, 0.504966887417)
# eff_Dict_DDT_unc[4000] = ( 0.00389814926776, 0.00368336257083, 0.00393080648412, 0.0039151483603)

# tau21 nominal with 0.45 cut:
# eff_Dict_DDT[600] = (0.566870, 0.554090, 0.093810, 0.133999)
# eff_Dict_DDT_unc[600] = (0.006849, 0.006824, 0.004030, 0.004677)
# eff_Dict_DDT[1000] = (0.592640, 0.560223, 0.116497, 0.163445)
# eff_Dict_DDT_unc[1000] = (0.005535, 0.005525, 0.003614, 0.004116)
# eff_Dict_DDT[2000] = (0.584481, 0.537029, 0.157280, 0.192418)
# eff_Dict_DDT_unc[2000] = (0.005174, 0.005235, 0.003822, 0.004138)
# eff_Dict_DDT[3000] = (0.551068, 0.490412, 0.180449, 0.217195)
# eff_Dict_DDT_unc[3000] = (0.005141, 0.005189, 0.003975, 0.004280)
# eff_Dict_DDT[4000] = (0.546798, 0.470933, 0.182373, 0.236117)
# eff_Dict_DDT_unc[4000] = (0.005151, 0.005198, 0.003996, 0.004423)

# tau21 DDT for VV
eff_Dict_DDT[600] = (0.085021, 0.083302, 0.622468, 0.644930)
eff_Dict_DDT_unc[600] = (0.003855, 0.003794, 0.006701, 0.006569)
eff_Dict_DDT[1000] = (0.150888, 0.137175, 0.615609, 0.624907)
eff_Dict_DDT_unc[1000] = (0.004032, 0.003830, 0.005480, 0.005389)
eff_Dict_DDT[2000] = (0.267387, 0.227683, 0.535104, 0.557968)
eff_Dict_DDT_unc[2000] = (0.004647, 0.004402, 0.005236, 0.005214)
eff_Dict_DDT[3000] = (0.308013, 0.250377, 0.487393, 0.530812)
eff_Dict_DDT_unc[3000] = (0.004772, 0.004497, 0.005166, 0.005180)
eff_Dict_DDT[4000] = (0.349218, 0.278091, 0.456736, 0.511931)
eff_Dict_DDT_unc[4000] = (0.004933, 0.004666, 0.005155, 0.005206)

c1 = getCanvas()
c1.GetFrame().SetFillColor(21)
c1.GetFrame().SetBorderSize(12)

frame = c1.DrawFrame(0, 0, 2200, 1)
# if "qZ" in label.split("_")[0] or label.find("qW")!=-1: frame = c1.DrawFrame(1.1,0.001, 6.2, 800.)
frame.GetYaxis().CenterTitle()
frame.GetYaxis().SetTitleSize(0.05)
frame.GetXaxis().SetTitleSize(0.05)
frame.GetXaxis().SetLabelSize(0.04)
frame.GetYaxis().SetLabelSize(0.04)
frame.GetYaxis().SetTitleOffset(1.15)
frame.GetXaxis().SetTitleOffset(1.05)
frame.GetXaxis().CenterTitle()
# frame.SetMinimum(0.)
# frame.SetMaximum(1)
frame.GetXaxis().SetNdivisions(508)
frame.GetYaxis().CenterTitle(True)
frame.GetXaxis().SetTitle("jet p_{T} [GeV]")
frame.GetYaxis().SetTitle("efficiency")

leg = ROOT.TLegend(0.498995, 0.6602591, 0.9446734, 0.9011917)
leg.SetTextSize(0.028)
leg.SetLineColor(1)
leg.SetShadowColor(0)
leg.SetLineStyle(1)
leg.SetLineWidth(1)
leg.SetFillColor(ROOT.kWhite)
# leg.SetFillStyle(0)
leg.SetMargin(0.35)
leg.SetBorderSize(1)

# gr_eff_pythia_0p55_LP = ROOT.TGraphErrors(len(masses))
# gr_eff_herwig_0p55_LP = ROOT.TGraphErrors(len(masses))

arr_effX_pythia_0p55_LP = []
arr_effY_pythia_0p55_LP = []
arr_effErrX_pythia_0p55_LP = []
arr_effErrY_pythia_0p55_LP = []
arr_effX_herwig_0p55_LP = []
arr_effY_herwig_0p55_LP = []
arr_effErrX_herwig_0p55_LP = []
arr_effErrY_herwig_0p55_LP = []

arr_effX_pythia_0p55_HP = []
arr_effY_pythia_0p55_HP = []
arr_effErrX_pythia_0p55_HP = []
arr_effErrY_pythia_0p55_HP = []
arr_effX_herwig_0p55_HP = []
arr_effY_herwig_0p55_HP = []
arr_effErrX_herwig_0p55_HP = []
arr_effErrY_herwig_0p55_HP = []

arr_effX_pythia_0p35_LP = []
arr_effY_pythia_0p35_LP = []
arr_effErrX_pythia_0p35_LP = []
arr_effErrY_pythia_0p35_LP = []
arr_effX_herwig_0p35_LP = []
arr_effY_herwig_0p35_LP = []
arr_effErrX_herwig_0p35_LP = []
arr_effErrY_herwig_0p35_LP = []

arr_effX_pythia_0p35_HP = []
arr_effY_pythia_0p35_HP = []
arr_effErrX_pythia_0p35_HP = []
arr_effErrY_pythia_0p35_HP = []
arr_effX_herwig_0p35_HP = []
arr_effY_herwig_0p35_HP = []
arr_effErrX_herwig_0p35_HP = []
arr_effErrY_herwig_0p35_HP = []


arr_effRatio_0p35_HP = []
arr_effRatioErr_0p35_HP = []
arr_effRatio_0p55_HP = []
arr_effRatioErr_0p55_HP = []
arr_effRatio_0p35_LP = []
arr_effRatioErr_0p35_LP = []
arr_effRatio_0p55_LP = []
arr_effRatioErr_0p55_LP = []

for mass, eff_set in eff_Dict_DDT.items():
    arr_effX_pythia_0p55_LP.append(mass/2)
    arr_effY_pythia_0p55_LP.append(eff_Dict_DDT[mass][2])
    arr_effErrX_pythia_0p55_LP.append(0)
    arr_effErrY_pythia_0p55_LP.append(eff_Dict_DDT_unc[mass][2])
    arr_effX_herwig_0p55_LP.append(mass/2)
    arr_effY_herwig_0p55_LP.append(eff_Dict_DDT[mass][3])
    arr_effErrX_herwig_0p55_LP.append(eff_Dict_DDT_unc[mass][3])
    arr_effErrY_herwig_0p55_LP.append(eff_Dict_DDT_unc[mass][3])

    arr_effX_pythia_0p55_HP.append(mass/2)
    arr_effY_pythia_0p55_HP.append(eff_Dict_DDT[mass][0])
    arr_effErrX_pythia_0p55_HP.append(0)
    arr_effErrY_pythia_0p55_HP.append(eff_Dict_DDT_unc[mass][0])
    arr_effX_herwig_0p55_HP.append(mass/2)
    arr_effY_herwig_0p55_HP.append(eff_Dict_DDT[mass][1])
    arr_effErrX_herwig_0p55_HP.append(eff_Dict_DDT_unc[mass][1])
    arr_effErrY_herwig_0p55_HP.append(eff_Dict_DDT_unc[mass][1])

    # arr_effX_pythia_0p35_LP.append(mass/2)
    # arr_effY_pythia_0p35_LP.append(eff_pythia_0p35_LP[mass][0])
    # arr_effErrX_pythia_0p35_LP.append(0)
    # arr_effErrY_pythia_0p35_LP.append(eff_pythia_0p35_LP[mass][1])
    # arr_effX_herwig_0p35_LP.append(mass/2)
    # arr_effY_herwig_0p35_LP.append(eff_herwig_0p35_LP[mass][0])
    # arr_effErrX_herwig_0p35_LP.append(eff_herwig_0p35_LP[mass][1])
    # arr_effErrY_herwig_0p35_LP.append(eff_herwig_0p35_LP[mass][1])

    # arr_effX_pythia_0p35_HP.append(mass/2)
    # arr_effY_pythia_0p35_HP.append(eff_pythia_0p35_HP[mass][0])
    # arr_effErrX_pythia_0p35_HP.append(0)
    # arr_effErrY_pythia_0p35_HP.append(eff_pythia_0p35_HP[mass][1])
    # arr_effX_herwig_0p35_HP.append(mass/2)
    # arr_effY_herwig_0p35_HP.append(eff_herwig_0p35_HP[mass][0])
    # arr_effErrX_herwig_0p35_HP.append(eff_herwig_0p35_HP[mass][1])
    # arr_effErrY_herwig_0p35_HP.append(eff_herwig_0p35_HP[mass][1])

    # do the ratio calculation and error propagation
    # arr_effRatio_0p35_HP.append(eff_herwig_0p35_HP[mass][0]/eff_pythia_0p35_HP[mass][0])
    # arr_effRatioErr_0p35_HP.append(eff_herwig_0p35_HP[mass][0]/eff_pythia_0p35_HP[mass][0]*sqrt((eff_herwig_0p35_HP[mass][1]/eff_herwig_0p35_HP[mass][0])**2 + (eff_pythia_0p35_HP[mass][1])/eff_pythia_0p35_HP[mass][0])**2)
    arr_effRatio_0p55_HP.append(eff_Dict_DDT[mass][1]/eff_Dict_DDT[mass][0])
    arr_effRatioErr_0p55_HP.append(eff_Dict_DDT[mass][1]/eff_Dict_DDT[mass][0]*sqrt((eff_Dict_DDT[mass][1]*.1/eff_Dict_DDT[mass][1])**2 + (eff_Dict_DDT[mass][0]*.1)/eff_Dict_DDT[mass][0])**2)
    # arr_effRatio_0p35_LP.append(eff_herwig_0p35_LP[mass][0]/eff_pythia_0p35_LP[mass][0])
    # arr_effRatioErr_0p35_LP.append(eff_herwig_0p35_LP[mass][0]/eff_pythia_0p35_LP[mass][0]*sqrt((eff_herwig_0p35_LP[mass][1]/eff_herwig_0p35_LP[mass][0])**2 + (eff_pythia_0p35_LP[mass][1])/eff_pythia_0p35_LP[mass][0])**2)
    arr_effRatio_0p55_LP.append(eff_Dict_DDT[mass][3]/eff_Dict_DDT[mass][2])
    arr_effRatioErr_0p55_LP.append(eff_Dict_DDT[mass][3]/eff_Dict_DDT[mass][2]*sqrt((eff_Dict_DDT[mass][3]*.1/eff_Dict_DDT[mass][3])**2 + (eff_Dict_DDT[mass][2]*.1)/eff_Dict_DDT[mass][2])**2)



gr_eff_pythia_0p55_LP = ROOT.TGraphErrors(len(eff_Dict_DDT), array('d', arr_effX_pythia_0p55_LP), array('d', arr_effY_pythia_0p55_LP), array('d', arr_effErrX_pythia_0p55_LP), array('d', arr_effErrY_pythia_0p55_LP))
gr_eff_herwig_0p55_LP = ROOT.TGraphErrors(len(eff_Dict_DDT), array('d', arr_effX_herwig_0p55_LP), array('d', arr_effY_herwig_0p55_LP), array('d', arr_effErrX_herwig_0p55_LP), array('d', arr_effErrY_herwig_0p55_LP))
gr_eff_pythia_0p55_HP = ROOT.TGraphErrors(len(eff_Dict_DDT), array('d', arr_effX_pythia_0p55_HP), array('d', arr_effY_pythia_0p55_HP), array('d', arr_effErrX_pythia_0p55_HP), array('d', arr_effErrY_pythia_0p55_HP))
gr_eff_herwig_0p55_HP = ROOT.TGraphErrors(len(eff_Dict_DDT), array('d', arr_effX_herwig_0p55_HP), array('d', arr_effY_herwig_0p55_HP), array('d', arr_effErrX_herwig_0p55_HP), array('d', arr_effErrY_herwig_0p55_HP))

# gr_eff_pythia_0p35_LP = ROOT.TGraphErrors(len(masses), array('d', arr_effX_pythia_0p35_LP), array('d', arr_effY_pythia_0p35_LP), array('d', arr_effErrX_pythia_0p35_LP), array('d', arr_effErrY_pythia_0p35_LP))
# gr_eff_herwig_0p35_LP = ROOT.TGraphErrors(len(masses), array('d', arr_effX_herwig_0p35_LP), array('d', arr_effY_herwig_0p35_LP), array('d', arr_effErrX_herwig_0p35_LP), array('d', arr_effErrY_herwig_0p35_LP))
# gr_eff_pythia_0p35_HP = ROOT.TGraphErrors(len(masses), array('d', arr_effX_pythia_0p35_HP), array('d', arr_effY_pythia_0p35_HP), array('d', arr_effErrX_pythia_0p35_HP), array('d', arr_effErrY_pythia_0p35_HP))
# gr_eff_herwig_0p35_HP = ROOT.TGraphErrors(len(masses), array('d', arr_effX_herwig_0p35_HP), array('d', arr_effY_herwig_0p35_HP), array('d', arr_effErrX_herwig_0p35_HP), array('d', arr_effErrY_herwig_0p35_HP))


gr_eff_pythia_0p55_LP.SetMarkerStyle(20)
gr_eff_pythia_0p55_LP.SetMarkerSize(1)
gr_eff_pythia_0p55_LP.SetMarkerColor(1)
gr_eff_pythia_0p55_LP.SetTitle("Pythia LP (WP 0.45)")
gr_eff_pythia_0p55_LP.Draw("P")

gr_eff_herwig_0p55_LP.SetMarkerStyle(24)
gr_eff_herwig_0p55_LP.SetMarkerSize(1)
gr_eff_herwig_0p55_LP.SetMarkerColor(1)
gr_eff_herwig_0p55_LP.SetTitle("Herwig LP (WP 0.45)")
gr_eff_herwig_0p55_LP.Draw("P")

gr_eff_pythia_0p55_HP.SetMarkerStyle(21)
gr_eff_pythia_0p55_HP.SetMarkerSize(1)
gr_eff_pythia_0p55_HP.SetMarkerColor(2)
gr_eff_pythia_0p55_HP.SetTitle("Pythia HP (WP 0.45)")
gr_eff_pythia_0p55_HP.Draw("P")

gr_eff_herwig_0p55_HP.SetMarkerStyle(25)
gr_eff_herwig_0p55_HP.SetMarkerSize(1)
gr_eff_herwig_0p55_HP.SetMarkerColor(2)
gr_eff_herwig_0p55_HP.SetTitle("Herwig HP (WP 0.45)")
gr_eff_herwig_0p55_HP.Draw("P")

# gr_eff_pythia_0p35_LP.SetMarkerStyle(20)
# gr_eff_pythia_0p35_LP.SetMarkerSize(1)
# gr_eff_pythia_0p35_LP.SetMarkerColor(3)
# gr_eff_pythia_0p35_LP.SetTitle("Pythia LP (WP 0.35)")
# gr_eff_pythia_0p35_LP.Draw("P")

# gr_eff_herwig_0p35_LP.SetMarkerStyle(24)
# gr_eff_herwig_0p35_LP.SetMarkerSize(1)
# gr_eff_herwig_0p35_LP.SetMarkerColor(3)
# gr_eff_herwig_0p35_LP.SetTitle("Herwig LP (WP 0.35)")
# gr_eff_herwig_0p35_LP.Draw("P")

# gr_eff_pythia_0p35_HP.SetMarkerStyle(21)
# gr_eff_pythia_0p35_HP.SetMarkerSize(1)
# gr_eff_pythia_0p35_HP.SetMarkerColor(4)
# gr_eff_pythia_0p35_HP.SetTitle("Pythia HP (WP 0.35)")
# gr_eff_pythia_0p35_HP.Draw("P")

# gr_eff_herwig_0p35_HP.SetMarkerStyle(25)
# gr_eff_herwig_0p35_HP.SetMarkerSize(1)
# gr_eff_herwig_0p35_HP.SetMarkerColor(4)
# gr_eff_herwig_0p35_HP.SetTitle("Herwig HP (WP 0.35)")
# gr_eff_herwig_0p35_HP.Draw("P")

frame.Draw('sameaxis')

leg.AddEntry(gr_eff_pythia_0p55_LP, gr_eff_pythia_0p55_LP.GetTitle(), "p")
leg.AddEntry(gr_eff_herwig_0p55_LP, gr_eff_herwig_0p55_LP.GetTitle(), "p")
leg.AddEntry(gr_eff_pythia_0p55_HP, gr_eff_pythia_0p55_HP.GetTitle(), "p")
leg.AddEntry(gr_eff_herwig_0p55_HP, gr_eff_herwig_0p55_HP.GetTitle(), "p")

# leg.AddEntry(gr_eff_pythia_0p35_LP, gr_eff_pythia_0p35_LP.GetTitle(), "p")
# leg.AddEntry(gr_eff_herwig_0p35_LP, gr_eff_herwig_0p35_LP.GetTitle(), "p")
# leg.AddEntry(gr_eff_pythia_0p35_HP, gr_eff_pythia_0p35_HP.GetTitle(), "p")
# leg.AddEntry(gr_eff_herwig_0p35_HP, gr_eff_herwig_0p35_HP.GetTitle(), "p")

leg.Draw()

CMS_lumi.CMS_lumi(c1, iPeriod, iPos)

c1.SaveAs("efficiencies.pdf")

# ratio plots

c2 = getCanvas("c2")
c2.GetFrame().SetFillColor(21)
c2.GetFrame().SetBorderSize(12)

frame2 = c2.DrawFrame(0, 0.6, 2200, 2.4)
frame2.GetYaxis().CenterTitle()
frame2.GetYaxis().SetTitleSize(0.05)
frame2.GetXaxis().SetTitleSize(0.05)
frame2.GetXaxis().SetLabelSize(0.04)
frame2.GetYaxis().SetLabelSize(0.04)
frame2.GetYaxis().SetTitleOffset(1.15)
frame2.GetXaxis().SetTitleOffset(1.05)
frame2.GetXaxis().CenterTitle()
# frame.SetMinimum(0.)
# frame.SetMaximum(1)
frame2.GetXaxis().SetNdivisions(508)
frame2.GetYaxis().CenterTitle(True)
frame2.GetXaxis().SetTitle("jet p_{T} [GeV]")
frame2.GetYaxis().SetTitle("efficiency(Herwig) / efficiency(Pythia)")

leg2 = ROOT.TLegend(0.498995, 0.6602591, 0.9446734, 0.9011917)
leg2.SetTextSize(0.028)
leg2.SetLineColor(1)
leg2.SetShadowColor(0)
leg2.SetLineStyle(1)
leg2.SetLineWidth(1)
leg2.SetFillColor(ROOT.kWhite)
# leg.SetFillStyle(0)
leg2.SetMargin(0.35)
leg2.SetBorderSize(1)

# gr_ratio_0p35_LP = ROOT.TGraphErrors(len(masses), array('d', arr_effX_pythia_0p35_LP), array('d', arr_effRatio_0p35_LP), array('d', arr_effErrX_pythia_0p35_LP), array('d', arr_effRatioErr_0p35_LP))
gr_ratio_0p55_LP = ROOT.TGraphErrors(len(eff_Dict_DDT), array('d', arr_effX_pythia_0p55_LP), array('d', arr_effRatio_0p55_LP), array('d', arr_effErrX_pythia_0p55_LP), array('d', arr_effRatioErr_0p55_LP))
# gr_ratio_0p35_HP = ROOT.TGraphErrors(len(masses), array('d', arr_effX_pythia_0p35_HP), array('d', arr_effRatio_0p35_HP), array('d', arr_effErrX_pythia_0p35_HP), array('d', arr_effRatioErr_0p35_HP))
gr_ratio_0p55_HP = ROOT.TGraphErrors(len(eff_Dict_DDT), array('d', arr_effX_pythia_0p55_HP), array('d', arr_effRatio_0p55_HP), array('d', arr_effErrX_pythia_0p55_HP), array('d', arr_effRatioErr_0p55_HP))

gr_ratio_0p55_LP.SetMarkerStyle(20)
gr_ratio_0p55_LP.SetMarkerSize(1)
gr_ratio_0p55_LP.SetMarkerColor(1)
gr_ratio_0p55_LP.SetTitle("LP (WP 0.45)")
gr_ratio_0p55_LP.Draw("P")
gr_ratio_0p55_HP.SetMarkerStyle(21)
gr_ratio_0p55_HP.SetMarkerSize(1)
gr_ratio_0p55_HP.SetMarkerColor(2)
gr_ratio_0p55_HP.SetTitle("HP (WP 0.45)")
gr_ratio_0p55_HP.Draw("P")

# gr_ratio_0p35_LP.SetMarkerStyle(20)
# gr_ratio_0p35_LP.SetMarkerSize(1)
# gr_ratio_0p35_LP.SetMarkerColor(3)
# gr_ratio_0p35_LP.SetTitle("LP (WP 0.35)")
# gr_ratio_0p35_LP.Draw("P")
# gr_ratio_0p35_HP.SetMarkerStyle(21)
# gr_ratio_0p35_HP.SetMarkerSize(1)
# gr_ratio_0p35_HP.SetMarkerColor(4)
# gr_ratio_0p35_HP.SetTitle("HP (WP 0.35)")
# gr_ratio_0p35_HP.Draw("P")

f1 = ROOT.TF1("myfit", "exp([0]+[1]/x)", 200, 2200)
f2 = ROOT.TF1("mypolynomial", "[0]+[1]*x+[2]*x^2+[3]*x^3", 200, 2200)
f3 = ROOT.TF1("linear", "[0]", 200, 2200)
# f1 = ROOT.TF1("myfit", "[0]*exp(-[1]*x)", 200, 2200)

ROOT.gStyle.SetOptFit(0)

gr_ratio_0p55_LP.Fit("linear")
fit_ratio_0p55_LP = gr_ratio_0p55_LP.GetFunction("linear")
fit_ratio_0p55_LP.SetLineColor(gr_ratio_0p55_LP.GetMarkerColor())
print(gr_ratio_0p55_LP.GetTitle(), "result at 200 GeV:", fit_ratio_0p55_LP.Eval(200))
unc_fit_0p55_LP = fit_ratio_0p55_LP.IntegralError(200-10, 200+10)/fit_ratio_0p55_LP.Integral(200-10, 200+10)
p_ratio_0p55_LP = ROOT.TMarker(200, fit_ratio_0p55_LP.Eval(200), 29)
p_ratio_0p55_LP.SetMarkerSize(1)
p_ratio_0p55_LP.SetMarkerColor(gr_ratio_0p55_LP.GetMarkerColor())
p_ratio_0p55_LP.Draw()

gr_ratio_0p55_HP.Fit("mypolynomial")
fit_ratio_0p55_HP = gr_ratio_0p55_HP.GetFunction("mypolynomial")
fit_ratio_0p55_HP.SetLineColor(gr_ratio_0p55_HP.GetMarkerColor())
print(gr_ratio_0p55_HP.GetTitle(), "result at 200 GeV:", fit_ratio_0p55_HP.Eval(200))
unc_fit_0p55_HP = fit_ratio_0p55_HP.IntegralError(200-10, 200+10)/fit_ratio_0p55_HP.Integral(200-10, 200+10)
p_ratio_0p55_HP = ROOT.TMarker(200, fit_ratio_0p55_HP.Eval(200), 29)
p_ratio_0p55_HP.SetMarkerSize(1)
p_ratio_0p55_HP.SetMarkerColor(gr_ratio_0p55_HP.GetMarkerColor())
p_ratio_0p55_HP.Draw()


# gr_ratio_0p35_LP.Fit("mypolynomial")
# fit_ratio_0p35_LP = gr_ratio_0p35_LP.GetFunction("mypolynomial")
# fit_ratio_0p35_LP.SetLineColor(gr_ratio_0p35_LP.GetMarkerColor())
# print(gr_ratio_0p35_LP.GetTitle(), "result at 200 GeV:", fit_ratio_0p35_LP.Eval(200))
# unc_fit_0p35_LP = fit_ratio_0p35_LP.IntegralError(200-10, 200+10)/fit_ratio_0p35_LP.Integral(200-10, 200+10)
# p_ratio_0p35_LP = ROOT.TMarker(200, fit_ratio_0p35_LP.Eval(200), 29)
# p_ratio_0p35_LP.SetMarkerSize(1)
# p_ratio_0p35_LP.SetMarkerColor(gr_ratio_0p35_LP.GetMarkerColor())
# p_ratio_0p35_LP.Draw()


# gr_ratio_0p35_HP.Fit("mypolynomial")
# fit_ratio_0p35_HP = gr_ratio_0p35_HP.GetFunction("mypolynomial")
# fit_ratio_0p35_HP.SetLineColor(gr_ratio_0p35_HP.GetMarkerColor())
# print(gr_ratio_0p35_HP.GetTitle(), "result at 200 GeV:", fit_ratio_0p35_HP.Eval(200))
# unc_fit_0p35_HP = fit_ratio_0p35_HP.IntegralError(200-10, 200+10)/fit_ratio_0p35_HP.Integral(200-10, 200+10)
# p_ratio_0p35_HP = ROOT.TMarker(200, fit_ratio_0p35_HP.Eval(200), 29)
# p_ratio_0p35_HP.SetMarkerSize(1)
# p_ratio_0p35_HP.SetMarkerColor(gr_ratio_0p35_HP.GetMarkerColor())
# p_ratio_0p35_HP.Draw()


frame2.Draw('sameaxis')

leg2.AddEntry(gr_ratio_0p55_LP, gr_ratio_0p55_LP.GetTitle(), "p")
leg2.AddEntry(gr_ratio_0p55_HP, gr_ratio_0p55_HP.GetTitle(), "p")
# leg2.AddEntry(gr_ratio_0p35_LP, gr_ratio_0p35_LP.GetTitle(), "p")
# leg2.AddEntry(gr_ratio_0p35_HP, gr_ratio_0p35_HP.GetTitle(), "p")

leg2.Draw()

CMS_lumi.CMS_lumi(c2, iPeriod, iPos)

c2.SaveAs("ratios.pdf")



### uncertainty plots

c3 = getCanvas("c3")
c3.GetFrame().SetFillColor(21)
c3.GetFrame().SetBorderSize(12)

frame3 = c2.DrawFrame(0, -.1, 2200, 0.6)
frame3.GetYaxis().CenterTitle()
frame3.GetYaxis().SetTitleSize(0.05)
frame3.GetXaxis().SetTitleSize(0.05)
frame3.GetXaxis().SetLabelSize(0.04)
frame3.GetYaxis().SetLabelSize(0.04)
frame3.GetYaxis().SetTitleOffset(1.15)
frame3.GetXaxis().SetTitleOffset(1.05)
frame3.GetXaxis().CenterTitle()
# frame.SetMinimum(0.)
# frame.SetMaximum(1)
frame3.GetXaxis().SetNdivisions(508)
frame3.GetYaxis().CenterTitle(True)
frame3.GetXaxis().SetTitle("jet p_{T} [GeV]")
frame3.GetYaxis().SetTitle("uncertainty")

leg3 = ROOT.TLegend(0.698995, 0.6602591, 0.9446734, 0.9011917)
leg3.SetTextSize(0.028)
leg3.SetLineColor(1)
leg3.SetShadowColor(0)
leg3.SetLineStyle(1)
leg3.SetLineWidth(1)
leg3.SetFillColor(ROOT.kWhite)
# leg.SetFillStyle(0)
leg3.SetMargin(0.35)
leg3.SetBorderSize(1)

unc_0p55_LP = []
unc_0p55_HP = []
# unc_0p35_LP = []
# unc_0p35_HP = []
unc_err_0p55_LP = []
unc_err_0p55_HP = []
# unc_err_0p35_LP = []
# unc_err_0p35_HP = []

unc_0p55_LP.append(0)
unc_0p55_HP.append(0)
# unc_0p35_LP.append(0)
# unc_0p35_HP.append(0)
unc_err_0p55_LP.append(unc_fit_0p55_LP)
unc_err_0p55_HP.append(unc_fit_0p55_HP)
# unc_err_0p35_LP.append(unc_fit_0p35_LP)
# unc_err_0p35_HP.append(unc_fit_0p35_HP)

# calculate difference to point at 200 GeV using the functions
for i in range(len(eff_Dict_DDT)):
    unc_0p55_LP.append(abs(gr_ratio_0p55_LP.Eval(mass/2)-fit_ratio_0p55_LP.Eval(200)))
    unc_0p55_HP.append(abs(gr_ratio_0p55_HP.Eval(mass/2)-fit_ratio_0p55_HP.Eval(200)))
    # unc_0p35_LP.append(abs(gr_ratio_0p35_LP.Eval(mass/2)-fit_ratio_0p35_LP.Eval(200)))
    # unc_0p35_HP.append(abs(gr_ratio_0p35_HP.Eval(mass/2)-fit_ratio_0p35_HP.Eval(200)))

    unc_err_0p55_LP.append(sqrt(unc_fit_0p55_LP**2 + (gr_ratio_0p55_LP.GetErrorY(i))**2))
    unc_err_0p55_HP.append(sqrt(unc_fit_0p55_HP**2 + (gr_ratio_0p55_HP.GetErrorY(i))**2))
    # unc_err_0p35_LP.append(sqrt(unc_fit_0p35_LP**2 + (gr_ratio_0p35_LP.GetErrorY(i))**2))
    # unc_err_0p35_HP.append(sqrt(unc_fit_0p35_HP**2 + (gr_ratio_0p35_HP.GetErrorY(i))**2))
    # print("ERROR", gr_ratio_0p55_LP.GetErrorY(i), unc_err_0p55_LP[-1])


print(unc_0p55_LP)
print(unc_0p55_HP)
print(unc_err_0p55_LP)
print(unc_err_0p55_HP)

gr_unc_0p55_LP = ROOT.TGraphErrors(len(eff_Dict_DDT)+1, array('d', [200]+arr_effX_pythia_0p55_LP), array('d', unc_0p55_LP), array('d', arr_effErrX_pythia_0p55_LP), array('d', unc_err_0p55_LP))
gr_unc_0p55_HP = ROOT.TGraphErrors(len(eff_Dict_DDT)+1, array('d', [200]+arr_effX_pythia_0p55_HP), array('d', unc_0p55_HP), array('d', arr_effErrX_pythia_0p55_LP), array('d', unc_err_0p55_HP))
# gr_unc_0p35_LP = ROOT.TGraphErrors(len(masses)+1, array('d', [200]+arr_effX_pythia_0p35_LP), array('d', unc_0p35_LP), array('d', arr_effErrX_pythia_0p35_LP), array('d', unc_err_0p35_LP))
# gr_unc_0p35_HP = ROOT.TGraphErrors(len(masses)+1, array('d', [200]+arr_effX_pythia_0p35_HP), array('d', unc_0p35_HP), array('d', arr_effErrX_pythia_0p35_LP), array('d', unc_err_0p35_HP))

gr_unc_0p55_LP.SetMarkerColor(gr_ratio_0p55_LP.GetMarkerColor())
gr_unc_0p55_HP.SetMarkerColor(gr_ratio_0p55_HP.GetMarkerColor())
# gr_unc_0p35_LP.SetMarkerColor(gr_ratio_0p35_LP.GetMarkerColor())
# gr_unc_0p35_HP.SetMarkerColor(gr_ratio_0p35_HP.GetMarkerColor())

gr_unc_0p55_LP.Draw("p")
gr_unc_0p55_HP.Draw("p")
# gr_unc_0p35_LP.Draw("p")
# gr_unc_0p35_HP.Draw("p")

f4 = ROOT.TF1("logunc", "[0]*log(x/200)", 200, 2200)

gr_unc_0p55_LP.Fit("logunc")
fit_unc_0p55_LP = gr_unc_0p55_LP.GetFunction("logunc")
fit_unc_0p55_LP.SetLineColor(gr_unc_0p55_LP.GetMarkerColor())
gr_unc_0p55_HP.Fit("logunc")
fit_unc_0p55_HP = gr_unc_0p55_HP.GetFunction("logunc")
fit_unc_0p55_HP.SetLineColor(gr_unc_0p55_HP.GetMarkerColor())
# gr_unc_0p35_LP.Fit("logunc")
# fit_unc_0p35_LP = gr_unc_0p35_LP.GetFunction("logunc")
# fit_unc_0p35_LP.SetLineColor(gr_unc_0p35_LP.GetMarkerColor())
# gr_unc_0p35_HP.Fit("logunc")
# fit_unc_0p35_HP = gr_unc_0p35_HP.GetFunction("logunc")
# fit_unc_0p35_HP.SetLineColor(gr_unc_0p35_HP.GetMarkerColor())

addInfo = ROOT.TPaveText(0.14, 0.5,
                         0.595302, 0.78, "NDC")
addInfo.SetFillColor(0)
addInfo.SetLineColor(0)
addInfo.SetFillStyle(0)
addInfo.SetBorderSize(0)
addInfo.SetTextFont(42)
addInfo.SetTextSize(0.040)
addInfo.SetTextAlign(12)

# addInfo.InsertText("{}: {:.1f}% #times ln(p_{{T}}/200 GeV)".format(gr_ratio_0p35_HP.GetTitle(), fit_unc_0p35_HP.GetParameter(0)*100))
# addInfo.InsertText("{}: {:.1f}% #times ln(p_{{T}}/200 GeV)".format(gr_ratio_0p35_LP.GetTitle(), fit_unc_0p35_LP.GetParameter(0)*100))
addInfo.InsertText("{}: {:.1f}% #times ln(p_{{T}}/200 GeV)".format(gr_ratio_0p55_HP.GetTitle(), fit_unc_0p55_HP.GetParameter(0)*100))
addInfo.InsertText("{}: {:.1f}% #times ln(p_{{T}}/200 GeV)".format(gr_ratio_0p55_LP.GetTitle(), 2*fit_unc_0p55_LP.GetParameter(0)*100))

# print("{}: {:.1f}% * ln(p_T/200 GeV)".format(gr_ratio_0p35_HP.GetTitle(), fit_unc_0p35_HP.GetParameter(0)*100))
# print("{}: {:.1f}% * ln(p_T/200 GeV)".format(gr_ratio_0p35_LP.GetTitle(), fit_unc_0p35_LP.GetParameter(0)*100))
print("{}: {:.1f}% * ln(p_T/200 GeV)".format(gr_ratio_0p55_HP.GetTitle(), fit_unc_0p55_HP.GetParameter(0)*100))
print("{}: {:.1f}% * ln(p_T/200 GeV)".format(gr_ratio_0p55_LP.GetTitle(), 2*fit_unc_0p55_LP.GetParameter(0)*100))

addInfo.Draw()

frame3.Draw('sameaxis')

leg3.AddEntry(gr_unc_0p55_LP, gr_ratio_0p55_LP.GetTitle(), "p")
leg3.AddEntry(gr_unc_0p55_HP, gr_ratio_0p55_HP.GetTitle(), "p")
# leg3.AddEntry(gr_unc_0p35_LP, gr_ratio_0p35_LP.GetTitle(), "p")
# leg3.AddEntry(gr_unc_0p35_HP, gr_ratio_0p35_HP.GetTitle(), "p")

leg3.Draw()

CMS_lumi.CMS_lumi(c3, iPeriod, iPos)

c3.SaveAs("uncertainties.pdf")
