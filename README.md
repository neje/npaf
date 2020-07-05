# npaf
## Network Performance Analysis Framework (NPAF)
NPAF framework is an extension of the **ns-3** simulator (https://www.nsnam.org/) that enables easy calculation of most frequently used nerwork key performance indicators (KPIs). These KPIs include: Throughput on application layer, Packet Loss Ratio (PLR), Useful Traffic Ratio (UTR) (this KPI works only for YansWiFiPhy for now!), and End-to-End (E2E) delay KPIs such as Min, Max, Average, Jitter and Histogram for all application layer data packets.

## Instalation instructions
1. Download ns-3 from https://www.nsnam.org/ and follow instructions from https://www.nsnam.org/wiki/Installation for installing prerequisits and instructions from ns-3 tutorial for compilation of ns-3 files.
2. Navigate to your **<ns-3_installation_directory>/contrib/** folder. 
3. Create new folder named **npaf** and copy files from this repository into **<ns-3_installation_directory>/contrib/npaf/** foldef.
Alternatively, you can clone this repository into **<ns-3_installation_directory>/contrib/** folder using command: git clone https://github.com/neje/npaf.git.
4. Navigate to your **<ns-3_installation_directory>/** folder. 
5. Reconfigure your ns-3 installation using **waf** command: ./waf configure (you can use all options you need). 
6. Compile your ns-3 installation **waf** command: ./waf build (you can use all options you need). 
7. Please note that this utility uses **namespace napaf**, so you should not forget to add this namespace to your scratches (for example you can add this line in your C++ code **using namespace npaf;**).

## Previous work
This utility is evolved from our previous work that is published in several papers. In this papers you can find deaper explanations of how this utility works, class diagrams, and several usecase scenarious used to verify functionality.  

### Papers
[1] 
[2] 
