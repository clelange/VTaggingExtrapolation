
import ROOT
from CMGTools.VVResonances.plotting.RooPlotter import *
from CMGTools.VVResonances.plotting.TreePlotter import TreePlotter
from CMGTools.VVResonances.plotting.MergedPlotter import MergedPlotter
from CMGTools.VVResonances.plotting.StackPlotter import StackPlotter
from CMGTools.VVResonances.plotting.tdrstyle import *
setTDRStyle()
from  CMGTools.VVResonances.plotting.CMS_lumi import *
import os
from array import array
from time import sleep
import optparse
import math

ROOT.gROOT.SetBatch(False)

H_ref = 600
W_ref = 800
W = W_ref
H  = H_ref

# directory='/eos/user/t/thaarres/www/vvana/control_plots'
lumi_13TeV = "41.4 fb^{-1}"
lumi_sqrtS = "13 TeV" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)
iPeriod=0
iPosX = 11
cuts={}
lumi='41367'

cuts['commonTOT'] = '(njj>0&&jj_LV_mass>1126&&abs(jj_l1_eta-jj_l2_eta)<1.3&&jj_l1_softDrop_mass>55.&&jj_l1_softDrop_mass<215.&&jj_l2_softDrop_mass>55.&&jj_l2_softDrop_mass<215.)'
cuts['commonTOT'] = '(njj>0&&abs(jj_l1_eta-jj_l2_eta)<1.3&&jj_l1_softDrop_mass>55.&&jj_l1_softDrop_mass<215.&&jj_l2_softDrop_mass>55.&&jj_l2_softDrop_mass<215.)'
cuts['commonTOT'] = '(jj_l1_mergedVTruth==1&&njj>0&&abs(jj_l1_eta-jj_l2_eta)<1.3)'
cat = {}
cat['HP1'] = '(jj_l1_tau2/jj_l1_tau1+(0.080*TMath::Log((jj_l1_softDrop_mass*jj_l1_softDrop_mass)/jj_l1_pt)))<0.43'
cat['HP2'] = '(jj_l2_tau2/jj_l2_tau1+(0.080*TMath::Log((jj_l2_softDrop_mass*jj_l2_softDrop_mass)/jj_l2_pt)))<0.43'
cat['LP1'] = '(jj_l1_tau2/jj_l1_tau1+(0.080*TMath::Log((jj_l1_softDrop_mass*jj_l1_softDrop_mass)/jj_l1_pt)))>0.43&&(jj_l1_tau2/jj_l1_tau1+(0.080*TMath::Log((jj_l1_softDrop_mass*jj_l1_softDrop_mass)/jj_l1_pt)))<0.79'
cat['LP2'] = '(jj_l2_tau2/jj_l2_tau1+(0.080*TMath::Log((jj_l2_softDrop_mass*jj_l2_softDrop_mass)/jj_l2_pt)))>0.43&&(jj_l2_tau2/jj_l2_tau1+(0.080*TMath::Log((jj_l2_softDrop_mass*jj_l2_softDrop_mass)/jj_l2_pt)))<0.79'
cat['HP1'] = '(jj_l1_tau2/jj_l1_tau1)<0.45'
cat['HP2'] = '(jj_l2_tau2/jj_l2_tau1)<0.45'
cat['LP1'] = '(jj_l1_tau2/jj_l1_tau1)>0.45&&(jj_l1_tau2/jj_l1_tau1)<0.75'
cat['LP2'] = '(jj_l2_tau2/jj_l2_tau1)>0.45&&(jj_l2_tau2/jj_l2_tau1)<0.75'

cuts['HPHP'] = '('+cat['HP1']+'&&'+cat['HP2']+')'
cuts['HPLP'] = '(('+cat['HP1']+'&&'+cat['LP2']+')||('+cat['LP1']+'&&'+cat['HP2']+'))'


def get_palette(mode):
 palette = {}
 palette['gv'] = []
 colors = ['#40004b','#762a83','#9970ab','#de77ae','#a6dba0','#5aae61','#1b7837','#00441b','#92c5de','#4393c3','#2166ac','#053061']
 colors = ['#762a83','#de77ae','#a6dba0','#92c5de','#4393c3','#2166ac','#053061']
 colors = ['#FF420E','#80BD9E','#a6dba0','#92c5de','#4393c3','#2166ac','#053061','#40004b','#762a83','#9970ab','#de77ae']
 for c in colors:
  palette['gv'].append(c)
 return palette[mode]

palette = get_palette('gv')
col = rt.TColor()

def sigmoidHP(x,p):
    max_eff = 0.235 #0.233
    return max_eff/(1+math.exp(-p[1]*(x[0]-p[0]))) # ptdep(HP) == 0.235/(1+math.exp(-0.004*(MH-954)))

def sigmoidLP(x,p):
    max_eff = 0.273 #0.064
    return max_eff/(1+math.exp(-p[1]*(x[0]-p[0]))) # ptdep(LP) == 0.273/(1+math.exp(-0.002*(MH-1296)))


def getCanvas(title):
	T = 0.08*H_ref
	B = 0.12*H_ref
	L = 0.12*W_ref
	R = 0.04*W_ref
	canvas = ROOT.TCanvas(title,title,50,50,W,H)
	canvas.SetFillColor(0)
	canvas.SetBorderMode(0)
	canvas.SetFrameFillStyle(0)
	canvas.SetFrameBorderMode(0)
	canvas.SetLeftMargin( L/W )
	canvas.SetRightMargin( R/W )
	canvas.SetTopMargin( T/H )
	canvas.SetBottomMargin( B/H )
	canvas.SetTickx(0)
	canvas.SetTicky(0)
	canvas.Update()
	ROOT.gStyle.SetOptStat(0)
	ROOT.gStyle.SetOptTitle(0)
	ROOT.gStyle.SetOptFit(0)

	legend = ROOT.TLegend(0.42,0.65,0.92,0.9,"","brNDC")
	legend.SetBorderSize(0)
	legend.SetLineColor(1)
	legend.SetLineStyle(1)
	legend.SetLineWidth(1)
	legend.SetFillColor(0)
	legend.SetFillStyle(0)
	legend.SetTextFont(42)

	return canvas, legend

if __name__ == '__main__':
  usage = 'usage: %prog [options]'
  parser = optparse.OptionParser(usage)
  parser.add_option('-f', '--folder'  , action='store', type='string', dest='folder', default='/eos/cms/store/cmst3/group/exovv/clange/HeppyProduction/EssentialThea/')
  parser.add_option('-o', '--output', action='store', type='string', dest='target', default='ptdep_out/')
  (options, args) = parser.parse_args()

  samples  = options.folder
  target   = options.target
  masses = [600.,1000.,2000.,3000.,4000.]
  template = "BulkGravToWW_narrow_M_"
  uncertianties_HP = []
  uncertianties_LP = []
  efficiencyHerwigHP = []
  efficiencyPythiaHP = []
  efficiencyHerwigLP = []
  efficiencyPythiaLP = []
  for m in masses:
    plotters=[]
    fnames = [samples+"BulkGravToWW_narrow_"+str(int(m)),samples+"BulkGravToWW_narrow_M_"+str(int(m))+"_herwigpp"]
    for filename in fnames:
      plotters.append(TreePlotter(filename+".root",'tree'))
      plotters[-1].setupFromFile(filename+'.pck')
      plotters[-1].addCorrectionFactor('xsec','tree')
      plotters[-1].addCorrectionFactor('genWeight','tree')
      plotters[-1].addCorrectionFactor('puWeight','tree')
    cutTAGHP ="(jj_l1_mergedVTruth==1&&njj>0&&abs(jj_l1_eta-jj_l2_eta)<1.3&&jj_l1_softDrop_mass>65.&&jj_l1_softDrop_mass<105.)&&(jj_l1_tau2/jj_l1_tau1)<0.45&&jj_l1_softDrop_mass>65.&&jj_l1_softDrop_mass<105."
    cutTAGLP ="(jj_l1_mergedVTruth==1&&njj>0&&abs(jj_l1_eta-jj_l2_eta)<1.3&&jj_l1_softDrop_mass>65.&&jj_l1_softDrop_mass<105.)&&(jj_l1_tau2/jj_l1_tau1)>0.45&&(jj_l1_tau2/jj_l1_tau1)<=0.75&&jj_l1_softDrop_mass>65.&&jj_l1_softDrop_mass<105."
    hPythia    = plotters[0].drawTH1("jj_l1_softDrop_mass",cuts['commonTOT'] ,"1", 300,   0.,300.  ,"M_{Softdrop}",'GeV'); hPythia    .SetName("hPythia_%i"%int(m))   ;
    hHerwig    = plotters[1].drawTH1("jj_l1_softDrop_mass",cuts['commonTOT'] ,"1", 300,   0.,300.  ,"M_{Softdrop}",'GeV'); hHerwig    .SetName("hHerwig_%i"%int(m))   ;
    hPythia_HP = plotters[0].drawTH1("jj_l1_softDrop_mass",cutTAGHP,          "1", 300,   0.,300.  ,"M_{Softdrop}",'GeV'); hPythia_HP .SetName("hPythia_HP_%i"%int(m));
    hHerwig_HP = plotters[1].drawTH1("jj_l1_softDrop_mass",cutTAGHP,          "1", 300,   0.,300.  ,"M_{Softdrop}",'GeV'); hHerwig_HP .SetName("hHerwig_HP_%i"%int(m));
    hPythia_LP = plotters[0].drawTH1("jj_l1_softDrop_mass",cutTAGLP,          "1", 300,   0.,300.  ,"M_{Softdrop}",'GeV'); hPythia_LP .SetName("hPythia_LP_%i"%int(m));
    hHerwig_LP = plotters[1].drawTH1("jj_l1_softDrop_mass",cutTAGLP,          "1", 300,   0.,300.  ,"M_{Softdrop}",'GeV'); hHerwig_LP .SetName("hHerwig_LP_%i"%int(m));
    efficiencyPythiaHP.append(hPythia_HP.GetEntries()/hPythia.GetEntries())
    efficiencyHerwigHP.append(hHerwig_HP.GetEntries()/hHerwig.GetEntries())
    efficiencyPythiaLP.append(hPythia_LP.GetEntries()/hPythia.GetEntries())
    efficiencyHerwigLP.append(hHerwig_LP.GetEntries()/hHerwig.GetEntries())

    uncertianty_HP = efficiencyHerwigHP[-1]/efficiencyPythiaHP[-1]-efficiencyHerwigHP[0]/efficiencyPythiaHP[0]
    uncertianty_LP = efficiencyHerwigLP[-1]/efficiencyPythiaLP[-1]-efficiencyHerwigLP[0]/efficiencyPythiaLP[0]

    # if m == 600.:
    #   uncertianties_HP.append(0.09)
    #   uncertianties_LP.append(0.09)
    #   print "HP ---- M = 600 GeV ---(Reference difference, pt 300 GeV): Eff Pythia = %.3f  Eff Herwig = %.3f EffHerwig/Effpythia-1 = %.3f " %(efficiencyPythiaHP[0],efficiencyHerwigHP[0],abs(efficiencyHerwigHP[0]/efficiencyPythiaHP[0]-1))
    #   print "LP ---- M = 600 GeV ---(Reference difference, pt 300 GeV): Eff Pythia = %.3f  Eff Herwig = %.3f EffHerwig/Effpythia-1 = %.3f " %(efficiencyPythiaLP[0],efficiencyHerwigLP[0],abs(efficiencyHerwigLP[0]/efficiencyPythiaLP[0]-1))
    # else:
    uncertianties_HP.append(abs(uncertianty_HP))
    uncertianties_LP.append(abs(uncertianty_LP))
      # print "M = %i GeV ---Eff Pythia = %.3f Eff Herwig = %.3f  EffHerwig/Effpythia-1 = %.3f (EffHerwig/Effpythia)-(EffHerwig_500GeV/EffPythia_500GeV) = %.3f" %(m,efficiencyPythiaHP[-1],efficiencyHerwigHP[-1],efficiencyHerwigHP[-1]/efficiencyPythiaHP[-1]-1, uncertianty_HP)
    print "HP ---- M = %i GeV --- EffPythia = %.3f EffHerwig = %.3f (EffHerwig/Effpythia)-(EffHerwig_600GeV/EffPythia_600GeV) = %.3f" %(m,efficiencyPythiaHP[-1],efficiencyHerwigHP[-1], abs(uncertianty_HP))
    print "LP ---- M = %i GeV --- EffPythia = %.3f EffHerwig = %.3f (EffHerwig/Effpythia)-(EffHerwig_600GeV/EffPythia_600GeV) = %.3f" %(m,efficiencyPythiaLP[-1],efficiencyHerwigLP[-1], abs(uncertianty_LP))

  masses = [300.,500.,1000.,1500.,2000.]
  # masses.append(2500.)
#   uncertianties_HP.append(uncertianties_HP[-1])
#   uncertianties_LP.append(uncertianties_LP[-1])
  vx = array("f",masses)
  vxErr = array("f",[x*.10 for x in masses])
  vy = array("f",uncertianties_HP)
  errs = [x*.10 for x in uncertianties_HP]
  vyErr = array("f",errs)
  vy_LP    = array("f",uncertianties_LP)
  errs_LP  = [x*.10 for x in uncertianties_LP]
  vyErr_LP = array("f",errs_LP)
  # vxErr = array("f",masses*0.1)
  gHP = rt.TGraphErrors(len(vx),vx,vy,vxErr,vyErr)
  gLP = rt.TGraphErrors(len(vx),vx,vy_LP,vxErr,vyErr_LP)
  # f = rt.TF1("ptdep", "pol3", 1000, 6000)
  # f_HP = rt.TF1("ptdep_HP", sigmoidHP, 600, 5000,2)
 #  f_LP = rt.TF1("ptdep_LP", sigmoidLP, 600, 5000,2)
  f_HP = rt.TF1("ptdep_HP", "[0]*log(x/300)", 500, 2000)
  f_LP = rt.TF1("ptdep_LP", "[0]*log(x/300)", 500, 2000)
  # f_HP.SetParameter(0,9.53469e+02)
#   f_HP.SetParameter(1,4.04425e-03)
#   f_LP.SetParameter(0,9.53469e+02)
#   f_LP.SetParameter(1,4.04425e-03)
  f_HP.SetParameter(0,0.08)
  f_LP.SetParameter(0,0.08)
#   f.SetParameter(1, 1.29963e-04)
#   f.SetParameter(2,-3.25678e-08)
#   f.SetParameter(3, 2.25082e-12)
  for i in range(0,10):
    gHP.Fit("ptdep_HP")#,"FERS")
    gLP.Fit("ptdep_LP")#,"FERS")

  gHP.SetMarkerSize(1.6)
  gLP.SetMarkerSize(1.6)
  gHP.SetMarkerStyle(20)
  gLP.SetMarkerStyle(20)
  gLP.GetYaxis().SetRangeUser(0.,0.50)
  gHP.SetMarkerColor(col.GetColor(palette[0]))
  gLP.SetMarkerColor(col.GetColor(palette[1]))
  gHP.SetLineColor(col.GetColor(palette[0]))
  gLP.SetLineColor(col.GetColor(palette[1]))

  c,leg = getCanvas("ptdep")
  leg.AddEntry(gHP,"HP","PE")
  leg.AddEntry(gLP,"LP","PE")
  gLP.Draw("APE")
  gHP.Draw("PEsame")
  leg.Draw("same")
  c.SaveAs("ptdep.png")
  sleep(10000)