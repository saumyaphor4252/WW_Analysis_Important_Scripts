void ratio_2j()
{
//=========Macro generated from canvas: c1/c1
//=========  (Wed May  7 23:40:31 2025) by ROOT version 6.14/09
   TCanvas *c1 = new TCanvas("c1", "c1",0,0,800,600);
   gStyle->SetOptStat(0);
   c1->SetHighLightColor(2);
   c1->Range(-25,-0.2499989,225,2.25);
   c1->SetFillColor(0);
   c1->SetBorderMode(0);
   c1->SetBorderSize(2);
   c1->SetFrameBorderMode(0);
   c1->SetFrameBorderMode(0);
   Double_t xAxis1[15] = {0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 140, 200}; 
   
   TH1D *histoDATA_rebinned__1 = new TH1D("histoDATA_rebinned__1","histo_DATA",14, xAxis1);
   histoDATA_rebinned__1->SetBinContent(1,1.067812);
   histoDATA_rebinned__1->SetBinContent(2,1.035961);
   histoDATA_rebinned__1->SetBinContent(3,0.9909668);
   histoDATA_rebinned__1->SetBinContent(4,1.004355);
   histoDATA_rebinned__1->SetBinContent(5,1.009856);
   histoDATA_rebinned__1->SetBinContent(6,0.9871048);
   histoDATA_rebinned__1->SetBinContent(7,0.9692837);
   histoDATA_rebinned__1->SetBinContent(8,0.9891909);
   histoDATA_rebinned__1->SetBinContent(9,0.9628007);
   histoDATA_rebinned__1->SetBinContent(10,0.9526845);
   histoDATA_rebinned__1->SetBinContent(11,0.9778217);
   histoDATA_rebinned__1->SetBinContent(12,0.9957514);
   histoDATA_rebinned__1->SetBinContent(13,0.9749502);
   histoDATA_rebinned__1->SetBinContent(14,1.057894);
   histoDATA_rebinned__1->SetBinError(1,0.04740774);
   histoDATA_rebinned__1->SetBinError(2,0.02718087);
   histoDATA_rebinned__1->SetBinError(3,0.02149813);
   histoDATA_rebinned__1->SetBinError(4,0.01911033);
   histoDATA_rebinned__1->SetBinError(5,0.01782569);
   histoDATA_rebinned__1->SetBinError(6,0.01699288);
   histoDATA_rebinned__1->SetBinError(7,0.016507);
   histoDATA_rebinned__1->SetBinError(8,0.01671597);
   histoDATA_rebinned__1->SetBinError(9,0.01681304);
   histoDATA_rebinned__1->SetBinError(10,0.01732727);
   histoDATA_rebinned__1->SetBinError(11,0.0184675);
   histoDATA_rebinned__1->SetBinError(12,0.01991755);
   histoDATA_rebinned__1->SetBinError(13,0.01574909);
   histoDATA_rebinned__1->SetBinError(14,0.01079813);
   histoDATA_rebinned__1->SetMinimum(1e-06);
   histoDATA_rebinned__1->SetMaximum(2);
   histoDATA_rebinned__1->SetEntries(29341.94);
   
   TF1 *tf91 = new TF1("tf9","pol9",0,200, TF1::EAddToList::kNo);
   tf91->SetFillColor(19);
   tf91->SetFillStyle(0);
   tf91->SetLineColor(2);
   tf91->SetLineWidth(2);
   tf91->SetChisquare(2.212541);
   tf91->SetNDF(4);
   tf91->GetXaxis()->SetLabelFont(42);
   tf91->GetXaxis()->SetLabelSize(0.035);
   tf91->GetXaxis()->SetTitleSize(0.035);
   tf91->GetXaxis()->SetTitleFont(42);
   tf91->GetYaxis()->SetLabelFont(42);
   tf91->GetYaxis()->SetLabelSize(0.035);
   tf91->GetYaxis()->SetTitleSize(0.035);
   tf91->GetYaxis()->SetTitleOffset(0);
   tf91->GetYaxis()->SetTitleFont(42);
   tf91->SetParameter(0,0.9281842);
   tf91->SetParError(0,0.2335243);
   tf91->SetParLimits(0,0,0);
   tf91->SetParameter(1,0.0546324);
   tf91->SetParError(1,0.07027845);
   tf91->SetParLimits(1,0,0);
   tf91->SetParameter(2,-0.006936282);
   tf91->SetParError(2,0.007338969);
   tf91->SetParLimits(2,0,0);
   tf91->SetParameter(3,0.0003847001);
   tf91->SetParError(3,0.000374846);
   tf91->SetParLimits(3,0,0);
   tf91->SetParameter(4,-1.157226e-05);
   tf91->SetParError(4,1.078506e-05);
   tf91->SetParLimits(4,0,0);
   tf91->SetParameter(5,2.055765e-07);
   tf91->SetParError(5,1.86333e-07);
   tf91->SetParLimits(5,0,0);
   tf91->SetParameter(6,-2.216467e-09);
   tf91->SetParError(6,1.96902e-09);
   tf91->SetParLimits(6,0,0);
   tf91->SetParameter(7,1.422417e-11);
   tf91->SetParError(7,1.243156e-11);
   tf91->SetParLimits(7,0,0);
   tf91->SetParameter(8,-4.984778e-14);
   tf91->SetParError(8,4.295144e-14);
   tf91->SetParLimits(8,0,0);
   tf91->SetParameter(9,7.322052e-17);
   tf91->SetParError(9,6.229796e-17);
   tf91->SetParLimits(9,0,0);
   tf91->SetParent(histoDATA_rebinned__1);
   histoDATA_rebinned__1->GetListOfFunctions()->Add(tf91);
   histoDATA_rebinned__1->SetMarkerStyle(20);
   histoDATA_rebinned__1->GetXaxis()->SetRange(1,20);
   histoDATA_rebinned__1->GetXaxis()->SetLabelFont(42);
   histoDATA_rebinned__1->GetXaxis()->SetLabelSize(0.035);
   histoDATA_rebinned__1->GetXaxis()->SetTitleSize(0.035);
   histoDATA_rebinned__1->GetXaxis()->SetTitleFont(42);
   histoDATA_rebinned__1->GetYaxis()->SetLabelFont(42);
   histoDATA_rebinned__1->GetYaxis()->SetLabelSize(0.035);
   histoDATA_rebinned__1->GetYaxis()->SetTitleSize(0.035);
   histoDATA_rebinned__1->GetYaxis()->SetTitleOffset(0);
   histoDATA_rebinned__1->GetYaxis()->SetTitleFont(42);
   histoDATA_rebinned__1->GetZaxis()->SetLabelFont(42);
   histoDATA_rebinned__1->GetZaxis()->SetLabelSize(0.035);
   histoDATA_rebinned__1->GetZaxis()->SetTitleSize(0.035);
   histoDATA_rebinned__1->GetZaxis()->SetTitleFont(42);
   histoDATA_rebinned__1->Draw("");
   
   TF1 *tf12 = new TF1("tf1","pol1",0,200, TF1::EAddToList::kDefault);
   tf12->SetFillColor(19);
   tf12->SetFillStyle(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#ff0000");
   tf12->SetLineColor(ci);
   tf12->SetLineWidth(2);
   tf12->SetChisquare(43.83697);
   tf12->SetNDF(12);
   tf12->GetXaxis()->SetLabelFont(42);
   tf12->GetXaxis()->SetLabelSize(0.035);
   tf12->GetXaxis()->SetTitleSize(0.035);
   tf12->GetXaxis()->SetTitleFont(42);
   tf12->GetYaxis()->SetLabelFont(42);
   tf12->GetYaxis()->SetLabelSize(0.035);
   tf12->GetYaxis()->SetTitleSize(0.035);
   tf12->GetYaxis()->SetTitleOffset(0);
   tf12->GetYaxis()->SetTitleFont(42);
   tf12->SetParameter(0,0.9701482);
   tf12->SetParError(0,0.01015742);
   tf12->SetParLimits(0,0,0);
   tf12->SetParameter(1,0.0003076381);
   tf12->SetParError(1,9.739298e-05);
   tf12->SetParLimits(1,0,0);
   tf12->Draw("same");
   
   TF1 *tf23 = new TF1("tf2","pol2",0,200, TF1::EAddToList::kDefault);
   tf23->SetFillColor(19);
   tf23->SetFillStyle(0);

   ci = TColor::GetColor("#00ff00");
   tf23->SetLineColor(ci);
   tf23->SetLineWidth(2);
   tf23->SetChisquare(7.265393);
   tf23->SetNDF(11);
   tf23->GetXaxis()->SetLabelFont(42);
   tf23->GetXaxis()->SetLabelSize(0.035);
   tf23->GetXaxis()->SetTitleSize(0.035);
   tf23->GetXaxis()->SetTitleFont(42);
   tf23->GetYaxis()->SetLabelFont(42);
   tf23->GetYaxis()->SetLabelSize(0.035);
   tf23->GetYaxis()->SetTitleSize(0.035);
   tf23->GetYaxis()->SetTitleOffset(0);
   tf23->GetYaxis()->SetTitleFont(42);
   tf23->SetParameter(0,1.066051);
   tf23->SetParError(0,0.01883247);
   tf23->SetParLimits(0,0,0);
   tf23->SetParameter(1,-0.00222025);
   tf23->SetParError(1,0.0004292054);
   tf23->SetParLimits(1,0,0);
   tf23->SetParameter(2,1.268454e-05);
   tf23->SetParError(2,2.097504e-06);
   tf23->SetParLimits(2,0,0);
   tf23->Draw("same");
   
   TF1 *tf34 = new TF1("tf3","pol3",0,200, TF1::EAddToList::kDefault);
   tf34->SetFillColor(19);
   tf34->SetFillStyle(0);

   ci = TColor::GetColor("#0000ff");
   tf34->SetLineColor(ci);
   tf34->SetLineWidth(2);
   tf34->SetChisquare(6.609105);
   tf34->SetNDF(10);
   tf34->GetXaxis()->SetLabelFont(42);
   tf34->GetXaxis()->SetLabelSize(0.035);
   tf34->GetXaxis()->SetTitleSize(0.035);
   tf34->GetXaxis()->SetTitleFont(42);
   tf34->GetYaxis()->SetLabelFont(42);
   tf34->GetYaxis()->SetLabelSize(0.035);
   tf34->GetYaxis()->SetTitleSize(0.035);
   tf34->GetYaxis()->SetTitleOffset(0);
   tf34->GetYaxis()->SetTitleFont(42);
   tf34->SetParameter(0,1.046196);
   tf34->SetParError(0,0.03090905);
   tf34->SetParLimits(0,0,0);
   tf34->SetParameter(1,-0.001229934);
   tf34->SetParError(1,0.001295596);
   tf34->SetParLimits(1,0,0);
   tf34->SetParameter(2,1.752474e-07);
   tf34->SetParError(2,1.558317e-05);
   tf34->SetParLimits(2,0,0);
   tf34->SetParameter(3,4.379432e-08);
   tf34->SetParError(3,5.405933e-08);
   tf34->SetParLimits(3,0,0);
   tf34->Draw("same");
   
   TF1 *tf45 = new TF1("tf4","pol4",0,200, TF1::EAddToList::kDefault);
   tf45->SetFillColor(19);
   tf45->SetFillStyle(0);

   ci = TColor::GetColor("#ff0033");
   tf45->SetLineColor(ci);
   tf45->SetLineWidth(2);
   tf45->SetChisquare(6.429437);
   tf45->SetNDF(9);
   tf45->GetXaxis()->SetLabelFont(42);
   tf45->GetXaxis()->SetLabelSize(0.035);
   tf45->GetXaxis()->SetTitleSize(0.035);
   tf45->GetXaxis()->SetTitleFont(42);
   tf45->GetYaxis()->SetLabelFont(42);
   tf45->GetYaxis()->SetLabelSize(0.035);
   tf45->GetYaxis()->SetTitleSize(0.035);
   tf45->GetYaxis()->SetTitleOffset(0);
   tf45->GetYaxis()->SetTitleFont(42);
   tf45->SetParameter(0,1.060707);
   tf45->SetParError(0,0.04612366);
   tf45->SetParLimits(0,0,0);
   tf45->SetParameter(1,-0.002410825);
   tf45->SetParError(1,0.003072473);
   tf45->SetParLimits(1,0,0);
   tf45->SetParameter(2,2.724503e-05);
   tf45->SetParError(2,6.573664e-05);
   tf45->SetParLimits(2,0,0);
   tf45->SetParameter(3,-1.852116e-07);
   tf45->SetParError(3,5.429675e-07);
   tf45->SetParLimits(3,0,0);
   tf45->SetParameter(4,6.339627e-10);
   tf45->SetParError(4,1.495642e-09);
   tf45->SetParLimits(4,0,0);
   tf45->Draw("same");
   
   TF1 *tf56 = new TF1("tf5","pol5",0,200, TF1::EAddToList::kDefault);
   tf56->SetFillColor(19);
   tf56->SetFillStyle(0);

   ci = TColor::GetColor("#ffcc00");
   tf56->SetLineColor(ci);
   tf56->SetLineWidth(2);
   tf56->SetChisquare(6.334425);
   tf56->SetNDF(8);
   tf56->GetXaxis()->SetLabelFont(42);
   tf56->GetXaxis()->SetLabelSize(0.035);
   tf56->GetXaxis()->SetTitleSize(0.035);
   tf56->GetXaxis()->SetTitleFont(42);
   tf56->GetYaxis()->SetLabelFont(42);
   tf56->GetYaxis()->SetLabelSize(0.035);
   tf56->GetYaxis()->SetTitleSize(0.035);
   tf56->GetYaxis()->SetTitleOffset(0);
   tf56->GetYaxis()->SetTitleFont(42);
   tf56->SetParameter(0,1.074483);
   tf56->SetParError(0,0.06422508);
   tf56->SetParLimits(0,0,0);
   tf56->SetParameter(1,-0.004096587);
   tf56->SetParError(1,0.006272954);
   tf56->SetParLimits(1,0,0);
   tf56->SetParameter(2,8.820533e-05);
   tf56->SetParError(2,0.0002084078);
   tf56->SetParLimits(2,0,0);
   tf56->SetParameter(3,-1.092236e-06);
   tf56->SetParError(3,2.992266e-06);
   tf56->SetParLimits(3,0,0);
   tf56->SetParameter(4,6.497026e-09);
   tf56->SetParError(4,1.90798e-08);
   tf56->SetParLimits(4,0,0);
   tf56->SetParameter(5,-1.359115e-11);
   tf56->SetParError(5,4.409272e-11);
   tf56->SetParLimits(5,0,0);
   tf56->Draw("same");
   
   TF1 *tf67 = new TF1("tf6","pol6",0,200, TF1::EAddToList::kDefault);
   tf67->SetFillColor(19);
   tf67->SetFillStyle(0);

   ci = TColor::GetColor("#cc00ff");
   tf67->SetLineColor(ci);
   tf67->SetLineWidth(2);
   tf67->SetChisquare(4.338431);
   tf67->SetNDF(7);
   tf67->GetXaxis()->SetLabelFont(42);
   tf67->GetXaxis()->SetLabelSize(0.035);
   tf67->GetXaxis()->SetTitleSize(0.035);
   tf67->GetXaxis()->SetTitleFont(42);
   tf67->GetYaxis()->SetLabelFont(42);
   tf67->GetYaxis()->SetLabelSize(0.035);
   tf67->GetYaxis()->SetTitleSize(0.035);
   tf67->GetYaxis()->SetTitleOffset(0);
   tf67->GetYaxis()->SetTitleFont(42);
   tf67->SetParameter(0,1.154136);
   tf67->SetParError(0,0.08546062);
   tf67->SetParLimits(0,0,0);
   tf67->SetParameter(1,-0.01795668);
   tf67->SetParError(1,0.01164447);
   tf67->SetParLimits(1,0,0);
   tf67->SetParameter(2,0.0008168714);
   tf67->SetParError(2,0.0005562767);
   tf67->SetParLimits(2,0,0);
   tf67->SetParameter(3,-1.774104e-05);
   tf67->SetParError(3,1.215825e-05);
   tf67->SetParLimits(3,0,0);
   tf67->SetParameter(4,1.913012e-07);
   tf67->SetParError(4,1.321916e-07);
   tf67->SetParLimits(4,0,0);
   tf67->SetParameter(5,-9.909272e-10);
   tf67->SetParError(5,6.931778e-10);
   tf67->SetParLimits(5,0,0);
   tf67->SetParameter(6,1.96504e-12);
   tf67->SetParError(6,1.390887e-12);
   tf67->SetParLimits(6,0,0);
   tf67->Draw("same");
   
   TF1 *tf78 = new TF1("tf7","pol7",0,200, TF1::EAddToList::kDefault);
   tf78->SetFillColor(19);
   tf78->SetFillStyle(0);

   ci = TColor::GetColor("#ffff00");
   tf78->SetLineColor(ci);
   tf78->SetLineWidth(2);
   tf78->SetChisquare(3.723104);
   tf78->SetNDF(6);
   tf78->GetXaxis()->SetLabelFont(42);
   tf78->GetXaxis()->SetLabelSize(0.035);
   tf78->GetXaxis()->SetTitleSize(0.035);
   tf78->GetXaxis()->SetTitleFont(42);
   tf78->GetYaxis()->SetLabelFont(42);
   tf78->GetYaxis()->SetLabelSize(0.035);
   tf78->GetYaxis()->SetTitleSize(0.035);
   tf78->GetYaxis()->SetTitleOffset(0);
   tf78->GetYaxis()->SetTitleFont(42);
   tf78->SetParameter(0,1.096816);
   tf78->SetParError(0,0.1124412);
   tf78->SetParLimits(0,0,0);
   tf78->SetParameter(1,-0.004598244);
   tf78->SetParError(1,0.02063005);
   tf78->SetParLimits(1,0,0);
   tf78->SetParameter(2,-0.0001386284);
   tf78->SetParError(2,0.001339095);
   tf78->SetParLimits(2,0,0);
   tf78->SetParameter(3,1.301467e-05);
   tf78->SetParError(3,4.104971e-05);
   tf78->SetParLimits(3,0,0);
   tf78->SetParameter(4,-3.196977e-07);
   tf78->SetParError(4,6.647065e-07);
   tf78->SetParLimits(4,0,0);
   tf78->SetParameter(5,3.547587e-09);
   tf78->SetParError(5,5.827143e-09);
   tf78->SetParLimits(5,0,0);
   tf78->SetParameter(6,-1.843585e-11);
   tf78->SetParError(6,2.604453e-11);
   tf78->SetParLimits(6,0,0);
   tf78->SetParameter(7,3.633895e-14);
   tf78->SetParError(7,4.632545e-14);
   tf78->SetParLimits(7,0,0);
   tf78->Draw("same");
   
   TF1 *tf89 = new TF1("tf8","pol8",0,200, TF1::EAddToList::kDefault);
   tf89->SetFillColor(19);
   tf89->SetFillStyle(0);

   ci = TColor::GetColor("#00ffff");
   tf89->SetLineColor(ci);
   tf89->SetLineWidth(2);
   tf89->SetChisquare(3.590944);
   tf89->SetNDF(5);
   tf89->GetXaxis()->SetLabelFont(42);
   tf89->GetXaxis()->SetLabelSize(0.035);
   tf89->GetXaxis()->SetTitleSize(0.035);
   tf89->GetXaxis()->SetTitleFont(42);
   tf89->GetYaxis()->SetLabelFont(42);
   tf89->GetYaxis()->SetLabelSize(0.035);
   tf89->GetYaxis()->SetTitleSize(0.035);
   tf89->GetYaxis()->SetTitleOffset(0);
   tf89->GetYaxis()->SetTitleFont(42);
   tf89->SetParameter(0,1.13488);
   tf89->SetParError(0,0.1536425);
   tf89->SetParLimits(0,0,0);
   tf89->SetParameter(1,-0.01569988);
   tf89->SetParError(1,0.03685331);
   tf89->SetParLimits(1,0,0);
   tf89->SetParameter(2,0.0008796098);
   tf89->SetParError(2,0.003104576);
   tf89->SetParLimits(2,0,0);
   tf89->SetParameter(3,-3.026288e-05);
   tf89->SetParError(3,0.0001259249);
   tf89->SetParLimits(3,0,0);
   tf89->SetParameter(4,6.690856e-07);
   tf89->SetParError(4,2.799952e-06);
   tf89->SetParLimits(4,0,0);
   tf89->SetParameter(5,-9.325604e-09);
   tf89->SetParError(5,3.588733e-08);
   tf89->SetParLimits(5,0,0);
   tf89->SetParameter(6,7.693836e-11);
   tf89->SetParError(6,2.636414e-10);
   tf89->SetParLimits(6,0,0);
   tf89->SetParameter(7,-3.369481e-13);
   tf89->SetParError(7,1.027868e-12);
   tf89->SetParLimits(7,0,0);
   tf89->SetParameter(8,5.972854e-16);
   tf89->SetParError(8,1.64299e-15);
   tf89->SetParLimits(8,0,0);
   tf89->Draw("same");
   
   TF1 *tf910 = new TF1("tf9","pol9",0,200, TF1::EAddToList::kDefault);
   tf910->SetFillColor(19);
   tf910->SetFillStyle(0);

   ci = TColor::GetColor("#ff00ff");
   tf910->SetLineColor(ci);
   tf910->SetLineWidth(2);
   tf910->SetChisquare(2.212541);
   tf910->SetNDF(4);
   tf910->GetXaxis()->SetLabelFont(42);
   tf910->GetXaxis()->SetLabelSize(0.035);
   tf910->GetXaxis()->SetTitleSize(0.035);
   tf910->GetXaxis()->SetTitleFont(42);
   tf910->GetYaxis()->SetLabelFont(42);
   tf910->GetYaxis()->SetLabelSize(0.035);
   tf910->GetYaxis()->SetTitleSize(0.035);
   tf910->GetYaxis()->SetTitleOffset(0);
   tf910->GetYaxis()->SetTitleFont(42);
   tf910->SetParameter(0,0.9281842);
   tf910->SetParError(0,0.2335243);
   tf910->SetParLimits(0,0,0);
   tf910->SetParameter(1,0.0546324);
   tf910->SetParError(1,0.07027845);
   tf910->SetParLimits(1,0,0);
   tf910->SetParameter(2,-0.006936282);
   tf910->SetParError(2,0.007338969);
   tf910->SetParLimits(2,0,0);
   tf910->SetParameter(3,0.0003847001);
   tf910->SetParError(3,0.000374846);
   tf910->SetParLimits(3,0,0);
   tf910->SetParameter(4,-1.157226e-05);
   tf910->SetParError(4,1.078506e-05);
   tf910->SetParLimits(4,0,0);
   tf910->SetParameter(5,2.055765e-07);
   tf910->SetParError(5,1.86333e-07);
   tf910->SetParLimits(5,0,0);
   tf910->SetParameter(6,-2.216467e-09);
   tf910->SetParError(6,1.96902e-09);
   tf910->SetParLimits(6,0,0);
   tf910->SetParameter(7,1.422417e-11);
   tf910->SetParError(7,1.243156e-11);
   tf910->SetParLimits(7,0,0);
   tf910->SetParameter(8,-4.984778e-14);
   tf910->SetParError(8,4.295144e-14);
   tf910->SetParLimits(8,0,0);
   tf910->SetParameter(9,7.322052e-17);
   tf910->SetParError(9,6.229796e-17);
   tf910->SetParLimits(9,0,0);
   tf910->Draw("same");
   
   TLegend *leg = new TLegend(0.7,0.7,0.9,0.9,NULL,"brNDC");
   leg->SetBorderSize(1);
   leg->SetLineColor(1);
   leg->SetLineStyle(1);
   leg->SetLineWidth(1);
   leg->SetFillColor(0);
   leg->SetFillStyle(1001);
   TLegendEntry *entry=leg->AddEntry("NULL","Polynomial Order","h");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("tf1","pol1 (chi2/NDF=3.65)","l");

   ci = TColor::GetColor("#ff0000");
   entry->SetLineColor(ci);
   entry->SetLineStyle(1);
   entry->SetLineWidth(2);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("tf2","pol2 (chi2/NDF=0.66)","l");

   ci = TColor::GetColor("#00ff00");
   entry->SetLineColor(ci);
   entry->SetLineStyle(1);
   entry->SetLineWidth(2);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("tf3","pol3 (chi2/NDF=0.66)","l");

   ci = TColor::GetColor("#0000ff");
   entry->SetLineColor(ci);
   entry->SetLineStyle(1);
   entry->SetLineWidth(2);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("tf4","pol4 (chi2/NDF=0.71)","l");

   ci = TColor::GetColor("#ff0033");
   entry->SetLineColor(ci);
   entry->SetLineStyle(1);
   entry->SetLineWidth(2);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("tf5","pol5 (chi2/NDF=0.79)","l");

   ci = TColor::GetColor("#ffcc00");
   entry->SetLineColor(ci);
   entry->SetLineStyle(1);
   entry->SetLineWidth(2);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("tf6","pol6 (chi2/NDF=0.62)","l");

   ci = TColor::GetColor("#cc00ff");
   entry->SetLineColor(ci);
   entry->SetLineStyle(1);
   entry->SetLineWidth(2);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("tf7","pol7 (chi2/NDF=0.62)","l");

   ci = TColor::GetColor("#ffff00");
   entry->SetLineColor(ci);
   entry->SetLineStyle(1);
   entry->SetLineWidth(2);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("tf8","pol8 (chi2/NDF=0.72)","l");

   ci = TColor::GetColor("#00ffff");
   entry->SetLineColor(ci);
   entry->SetLineStyle(1);
   entry->SetLineWidth(2);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("tf9","pol9 (chi2/NDF=0.55)","l");

   ci = TColor::GetColor("#ff00ff");
   entry->SetLineColor(ci);
   entry->SetLineStyle(1);
   entry->SetLineWidth(2);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   leg->Draw();
   
   TPaveText *pt = new TPaveText(0.3857286,0.9362587,0.6142714,0.995,"blNDC");
   pt->SetName("title");
   pt->SetBorderSize(0);
   pt->SetFillColor(0);
   pt->SetFillStyle(0);
   pt->SetTextFont(42);
   TText *pt_LaTex = pt->AddText("histo_DATA");
   pt->Draw();
   c1->Modified();
   c1->cd();
   c1->SetSelected(c1);
}
