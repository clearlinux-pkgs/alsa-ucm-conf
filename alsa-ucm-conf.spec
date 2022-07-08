#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x8380596DA6E59C91 (release@alsa-project.org)
#
Name     : alsa-ucm-conf
Version  : 1.2.7.2
Release  : 11
URL      : https://www.alsa-project.org/files/pub/lib/alsa-ucm-conf-1.2.7.2.tar.bz2
Source0  : https://www.alsa-project.org/files/pub/lib/alsa-ucm-conf-1.2.7.2.tar.bz2
Source1  : https://www.alsa-project.org/files/pub/lib/alsa-ucm-conf-1.2.7.2.tar.bz2.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: alsa-ucm-conf-data = %{version}-%{release}
Requires: alsa-ucm-conf-license = %{version}-%{release}
Patch1: 0001-Add-Makefile-to-make-packaging-ucm2-easier.patch

%description
# alsa-ucm-conf
## ALSA Use Case Manager configuration
### Installation
Copy the ucm and ucm2 trees to the alsa-lib configuration directory
(usually located in /usr/share/alsa) including symlinks. The files
files are extra (only informational).

%package data
Summary: data components for the alsa-ucm-conf package.
Group: Data

%description data
data components for the alsa-ucm-conf package.


%package license
Summary: license components for the alsa-ucm-conf package.
Group: Default

%description license
license components for the alsa-ucm-conf package.


%prep
%setup -q -n alsa-ucm-conf-1.2.7.2
cd %{_builddir}/alsa-ucm-conf-1.2.7.2
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1657310897
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1657310897
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/alsa-ucm-conf
cp %{_builddir}/alsa-ucm-conf-1.2.7.2/LICENSE %{buildroot}/usr/share/package-licenses/alsa-ucm-conf/27f14a443d8b2c78e6684ac3bb2fee5d8364c78f
%make_install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/alsa/ucm2/HDA/DualCodecs/DualCodecs.conf
/usr/share/alsa/ucm2/HDA/DualCodecs/HiFi.conf
/usr/share/alsa/ucm2/HDA/HDA-Capture-value.conf
/usr/share/alsa/ucm2/HDA/HDA.conf
/usr/share/alsa/ucm2/HDA/Hdmi.conf
/usr/share/alsa/ucm2/HDA/HiFi-acp.conf
/usr/share/alsa/ucm2/HDA/HiFi-analog.conf
/usr/share/alsa/ucm2/HDA/HiFi.conf
/usr/share/alsa/ucm2/HDA/init.conf
/usr/share/alsa/ucm2/Intel/SOF/HiFi.conf
/usr/share/alsa/ucm2/Intel/SOF/SOF.conf
/usr/share/alsa/ucm2/Intel/bdw-rt5677/HiFi.conf
/usr/share/alsa/ucm2/Intel/bdw-rt5677/bdw-rt5677.conf
/usr/share/alsa/ucm2/Intel/broadwell-rt286/HiFi.conf
/usr/share/alsa/ucm2/Intel/broadwell-rt286/broadwell-rt286.conf
/usr/share/alsa/ucm2/Intel/broxton-rt298/Hdmi.conf
/usr/share/alsa/ucm2/Intel/broxton-rt298/HiFi.conf
/usr/share/alsa/ucm2/Intel/broxton-rt298/broxton-rt298.conf
/usr/share/alsa/ucm2/Intel/bytcht-cx2072x/HiFi.conf
/usr/share/alsa/ucm2/Intel/bytcht-cx2072x/bytcht-cx2072x.conf
/usr/share/alsa/ucm2/Intel/bytcht-es8316/HiFi-Components.conf
/usr/share/alsa/ucm2/Intel/bytcht-es8316/HiFi-LongName.conf
/usr/share/alsa/ucm2/Intel/bytcht-es8316/HiFi.conf
/usr/share/alsa/ucm2/Intel/bytcht-es8316/bytcht-es8316.conf
/usr/share/alsa/ucm2/Intel/bytcr-rt5640/HiFi-Components.conf
/usr/share/alsa/ucm2/Intel/bytcr-rt5640/HiFi-LongName.conf
/usr/share/alsa/ucm2/Intel/bytcr-rt5640/HiFi.conf
/usr/share/alsa/ucm2/Intel/bytcr-rt5640/bytcr-rt5640.conf
/usr/share/alsa/ucm2/Intel/bytcr-rt5651/HiFi-Components.conf
/usr/share/alsa/ucm2/Intel/bytcr-rt5651/HiFi-LongName.conf
/usr/share/alsa/ucm2/Intel/bytcr-rt5651/HiFi.conf
/usr/share/alsa/ucm2/Intel/bytcr-rt5651/bytcr-rt5651.conf
/usr/share/alsa/ucm2/Intel/bytcr-wm5102/HiFi.conf
/usr/share/alsa/ucm2/Intel/bytcr-wm5102/bytcr-wm5102.conf
/usr/share/alsa/ucm2/Intel/cht-bsw-rt5672/HiFi.conf
/usr/share/alsa/ucm2/Intel/cht-bsw-rt5672/cht-bsw-rt5672.conf
/usr/share/alsa/ucm2/Intel/chtmax98090/HiFi.conf
/usr/share/alsa/ucm2/Intel/chtmax98090/chtmax98090.conf
/usr/share/alsa/ucm2/Intel/chtnau8824/HiFi.conf
/usr/share/alsa/ucm2/Intel/chtnau8824/chtnau8824.conf
/usr/share/alsa/ucm2/Intel/chtrt5645/HiFi.conf
/usr/share/alsa/ucm2/Intel/chtrt5645/chtrt5645.conf
/usr/share/alsa/ucm2/Intel/chtrt5650/HiFi.conf
/usr/share/alsa/ucm2/Intel/chtrt5650/chtrt5650.conf
/usr/share/alsa/ucm2/Intel/hda-dsp/Hdmi1.conf
/usr/share/alsa/ucm2/Intel/hda-dsp/Hdmi2.conf
/usr/share/alsa/ucm2/Intel/hda-dsp/HiFi.conf
/usr/share/alsa/ucm2/Intel/hda-dsp/hda-dsp.conf
/usr/share/alsa/ucm2/Intel/kblrt5660/Hdmi1.conf
/usr/share/alsa/ucm2/Intel/kblrt5660/Hdmi2.conf
/usr/share/alsa/ucm2/Intel/kblrt5660/HiFi.conf
/usr/share/alsa/ucm2/Intel/kblrt5660/kblrt5660.conf
/usr/share/alsa/ucm2/Intel/skylake-rt286/Hdmi1.conf
/usr/share/alsa/ucm2/Intel/skylake-rt286/Hdmi2.conf
/usr/share/alsa/ucm2/Intel/skylake-rt286/HiFi.conf
/usr/share/alsa/ucm2/Intel/skylake-rt286/skylake-rt286.conf
/usr/share/alsa/ucm2/Intel/sof-ehl-rt5660/Hdmi.conf
/usr/share/alsa/ucm2/Intel/sof-ehl-rt5660/HiFi.conf
/usr/share/alsa/ucm2/Intel/sof-ehl-rt5660/sof-ehl-rt5660.conf
/usr/share/alsa/ucm2/Intel/sof-essx8336/Hdmi.conf
/usr/share/alsa/ucm2/Intel/sof-essx8336/HiFi.conf
/usr/share/alsa/ucm2/Intel/sof-essx8336/sof-essx8336.conf
/usr/share/alsa/ucm2/Intel/sof-hda-dsp/Hdmi.conf
/usr/share/alsa/ucm2/Intel/sof-hda-dsp/HiFi.conf
/usr/share/alsa/ucm2/Intel/sof-hda-dsp/sof-hda-dsp.conf
/usr/share/alsa/ucm2/MediaTek/mt8195_demo/HiFi.conf
/usr/share/alsa/ucm2/MediaTek/mt8195_demo/mt8195_demo.conf
/usr/share/alsa/ucm2/MediaTek/mtk-rt5650/HDMI.conf
/usr/share/alsa/ucm2/MediaTek/mtk-rt5650/HiFi.conf
/usr/share/alsa/ucm2/MediaTek/mtk-rt5650/init.conf
/usr/share/alsa/ucm2/MediaTek/mtk-rt5650/mtk-rt5650.conf
/usr/share/alsa/ucm2/NXP/iMX8/Librem_5_Devkit/HiFi.conf
"/usr/share/alsa/ucm2/NXP/iMX8/Librem_5_Devkit/Librem 5 Devkit.conf"
/usr/share/alsa/ucm2/OMAP/abe-twl6040/Pandaboard/FMAnalog.conf
/usr/share/alsa/ucm2/OMAP/abe-twl6040/Pandaboard/HiFi.conf
/usr/share/alsa/ucm2/OMAP/abe-twl6040/Pandaboard/HiFiLP.conf
/usr/share/alsa/ucm2/OMAP/abe-twl6040/Pandaboard/Pandaboard.conf
/usr/share/alsa/ucm2/OMAP/abe-twl6040/Pandaboard/Record.conf
/usr/share/alsa/ucm2/OMAP/abe-twl6040/Pandaboard/Voice.conf
/usr/share/alsa/ucm2/OMAP/abe-twl6040/Pandaboard/VoiceCall.conf
/usr/share/alsa/ucm2/OMAP/abe-twl6040/SDP4430/FMAnalog.conf
/usr/share/alsa/ucm2/OMAP/abe-twl6040/SDP4430/HiFi.conf
/usr/share/alsa/ucm2/OMAP/abe-twl6040/SDP4430/HiFiLP.conf
/usr/share/alsa/ucm2/OMAP/abe-twl6040/SDP4430/Record.conf
/usr/share/alsa/ucm2/OMAP/abe-twl6040/SDP4430/SDP4430.conf
/usr/share/alsa/ucm2/OMAP/abe-twl6040/SDP4430/Voice.conf
/usr/share/alsa/ucm2/OMAP/abe-twl6040/SDP4430/VoiceCall.conf
/usr/share/alsa/ucm2/OMAP/abe-twl6040/abe-twl6040.conf
/usr/share/alsa/ucm2/Qualcomm/apq8016-sbc/HDMI.conf
/usr/share/alsa/ucm2/Qualcomm/apq8016-sbc/HiFi.conf
/usr/share/alsa/ucm2/Qualcomm/apq8016-sbc/apq8016-sbc.conf
/usr/share/alsa/ucm2/Qualcomm/apq8096/HDMI.conf
/usr/share/alsa/ucm2/Qualcomm/apq8096/HiFi.conf
/usr/share/alsa/ucm2/Qualcomm/apq8096/apq8096.conf
/usr/share/alsa/ucm2/Qualcomm/sc7180/rt5682-max98357a/HiFi.conf
/usr/share/alsa/ucm2/Qualcomm/sc7180/rt5682-max98357a/init.conf
/usr/share/alsa/ucm2/Qualcomm/sc7180/rt5682-max98357a/sc7180-rt5682-max98357a-1mic.conf
/usr/share/alsa/ucm2/Qualcomm/sdm845/HDMI.conf
/usr/share/alsa/ucm2/Qualcomm/sdm845/HiFi.conf
/usr/share/alsa/ucm2/Qualcomm/sdm845/sdm845.conf
/usr/share/alsa/ucm2/Qualcomm/sm8250/HDMI.conf
/usr/share/alsa/ucm2/Qualcomm/sm8250/HiFi.conf
/usr/share/alsa/ucm2/Qualcomm/sm8250/Qualcomm-RB5-WSA8815-Speakers-DMIC0.conf
/usr/share/alsa/ucm2/README.md
/usr/share/alsa/ucm2/Rockchip/es8316/HiFi.conf
/usr/share/alsa/ucm2/Rockchip/es8316/es8316.conf
/usr/share/alsa/ucm2/Rockchip/max98090/HiFi.conf
/usr/share/alsa/ucm2/Rockchip/max98090/max98090.conf
/usr/share/alsa/ucm2/Rockchip/rk3399-gru-sound/HiFi.conf
/usr/share/alsa/ucm2/Rockchip/rk3399-gru-sound/rk3399-gru-sound.conf
/usr/share/alsa/ucm2/Samsung/snow/HiFi.conf
/usr/share/alsa/ucm2/Samsung/snow/snow.conf
/usr/share/alsa/ucm2/Tegra/alc5632/HiFi.conf
/usr/share/alsa/ucm2/Tegra/alc5632/Record.conf
/usr/share/alsa/ucm2/Tegra/alc5632/alc5632.conf
/usr/share/alsa/ucm2/Tegra/max98090/HiFi.conf
/usr/share/alsa/ucm2/Tegra/max98090/max98090.conf
/usr/share/alsa/ucm2/Tegra/rt5640/Google-Nexus-7-HiFi.conf
/usr/share/alsa/ucm2/Tegra/rt5640/Google-Nexus-7.conf
/usr/share/alsa/ucm2/Tegra/tegra-hda/tegra-hda-HiFi.conf
/usr/share/alsa/ucm2/Tegra/tegra-hda/tegra-hda.conf
/usr/share/alsa/ucm2/Tegra/wm8903/Acer-A500-HiFi.conf
/usr/share/alsa/ucm2/Tegra/wm8903/Acer-A500.conf
/usr/share/alsa/ucm2/USB-Audio/Arturia/Minifuse-2-HiFi.conf
/usr/share/alsa/ucm2/USB-Audio/Arturia/Minifuse-2.conf
/usr/share/alsa/ucm2/USB-Audio/Audient/Audient-iD4-0003.conf
/usr/share/alsa/ucm2/USB-Audio/Audient/Audient-iD4-0009.conf
/usr/share/alsa/ucm2/USB-Audio/Audient/Audient-iD4-HiFi-0003.conf
/usr/share/alsa/ucm2/USB-Audio/Audient/Audient-iD4-HiFi-0009.conf
/usr/share/alsa/ucm2/USB-Audio/Behringer/Flow8-Recording-Hifi.conf
/usr/share/alsa/ucm2/USB-Audio/Behringer/Flow8-Recording.conf
/usr/share/alsa/ucm2/USB-Audio/Behringer/Flow8-Streaming-Hifi.conf
/usr/share/alsa/ucm2/USB-Audio/Behringer/Flow8-Streaming.conf
/usr/share/alsa/ucm2/USB-Audio/Behringer/UMC204HD-HiFi.conf
/usr/share/alsa/ucm2/USB-Audio/Behringer/UMC204HD.conf
/usr/share/alsa/ucm2/USB-Audio/Dell/Desktop-Front-Speaker-Headset.conf
/usr/share/alsa/ucm2/USB-Audio/Dell/Desktop-Front.conf
/usr/share/alsa/ucm2/USB-Audio/Dell/Desktop-Rear-Line.conf
/usr/share/alsa/ucm2/USB-Audio/Dell/Desktop-Rear.conf
/usr/share/alsa/ucm2/USB-Audio/Dell/WD15-Dock-HiFi.conf
/usr/share/alsa/ucm2/USB-Audio/Dell/WD15-Dock.conf
/usr/share/alsa/ucm2/USB-Audio/Gigabyte/Aorus-Master-Main-Audio-HiFi.conf
/usr/share/alsa/ucm2/USB-Audio/Gigabyte/Aorus-Master-Main-Audio.conf
/usr/share/alsa/ucm2/USB-Audio/GoXLR/GoXLR-HiFi.conf
/usr/share/alsa/ucm2/USB-Audio/GoXLR/GoXLR.conf
/usr/share/alsa/ucm2/USB-Audio/Lenovo/ThinkStation-P620-Main-HiFi.conf
/usr/share/alsa/ucm2/USB-Audio/Lenovo/ThinkStation-P620-Main.conf
/usr/share/alsa/ucm2/USB-Audio/Lenovo/ThinkStation-P620-Rear-HiFi.conf
/usr/share/alsa/ucm2/USB-Audio/Lenovo/ThinkStation-P620-Rear.conf
/usr/share/alsa/ucm2/USB-Audio/MOTU/M4-HiFi.conf
/usr/share/alsa/ucm2/USB-Audio/MOTU/M4.conf
/usr/share/alsa/ucm2/USB-Audio/NativeInstruments/Traktor-Kontrol-Z1-Mixer.conf
/usr/share/alsa/ucm2/USB-Audio/NativeInstruments/Traktor-Kontrol-Z1.conf
/usr/share/alsa/ucm2/USB-Audio/Realtek/ALC1220-VB-Desktop-HiFi.conf
/usr/share/alsa/ucm2/USB-Audio/Realtek/ALC1220-VB-Desktop.conf
/usr/share/alsa/ucm2/USB-Audio/Realtek/ALC4080-HiFi.conf
/usr/share/alsa/ucm2/USB-Audio/Realtek/ALC4080.conf
/usr/share/alsa/ucm2/USB-Audio/Steinberg/UR44-HiFi.conf
/usr/share/alsa/ucm2/USB-Audio/Steinberg/UR44.conf
/usr/share/alsa/ucm2/USB-Audio/USB-Audio.conf
/usr/share/alsa/ucm2/codecs/cx2072x/DisableSeq.conf
/usr/share/alsa/ucm2/codecs/cx2072x/EnableSeq.conf
/usr/share/alsa/ucm2/codecs/cx2072x/HeadPhones.conf
/usr/share/alsa/ucm2/codecs/cx2072x/HeadsetMic.conf
/usr/share/alsa/ucm2/codecs/cx2072x/InternalMic.conf
/usr/share/alsa/ucm2/codecs/cx2072x/Speaker.conf
/usr/share/alsa/ucm2/codecs/es8316/EnableSeq.conf
/usr/share/alsa/ucm2/codecs/es8316/HeadPhones.conf
/usr/share/alsa/ucm2/codecs/es8316/IN1-HeadsetMic.conf
/usr/share/alsa/ucm2/codecs/es8316/IN1-InternalMic.conf
/usr/share/alsa/ucm2/codecs/es8316/IN2-HeadsetMic.conf
/usr/share/alsa/ucm2/codecs/es8316/IN2-InternalMic.conf
/usr/share/alsa/ucm2/codecs/es8316/MonoSpeaker.conf
/usr/share/alsa/ucm2/codecs/es8316/Speaker.conf
/usr/share/alsa/ucm2/codecs/hda/hdmi.conf
/usr/share/alsa/ucm2/codecs/max98090/EnableSeq.conf
/usr/share/alsa/ucm2/codecs/max98090/Headphones.conf
/usr/share/alsa/ucm2/codecs/max98090/HeadsetMic.conf
/usr/share/alsa/ucm2/codecs/max98090/InternalMic.conf
/usr/share/alsa/ucm2/codecs/max98090/Speaker.conf
/usr/share/alsa/ucm2/codecs/nau8824/DMIC1_2.conf
/usr/share/alsa/ucm2/codecs/nau8824/EnableSeq.conf
/usr/share/alsa/ucm2/codecs/nau8824/HeadPhones.conf
/usr/share/alsa/ucm2/codecs/nau8824/HeadsetMic.conf
/usr/share/alsa/ucm2/codecs/nau8824/InternalMic.conf
/usr/share/alsa/ucm2/codecs/nau8824/MonoSpeaker.conf
/usr/share/alsa/ucm2/codecs/nau8824/Speaker.conf
/usr/share/alsa/ucm2/codecs/qcom-lpass/va-macro/DMIC0DisableSeq.conf
/usr/share/alsa/ucm2/codecs/qcom-lpass/va-macro/DMIC0EnableSeq.conf
/usr/share/alsa/ucm2/codecs/qcom-lpass/wsa-macro/SpeakerDisableSeq.conf
/usr/share/alsa/ucm2/codecs/qcom-lpass/wsa-macro/SpeakerEnableSeq.conf
/usr/share/alsa/ucm2/codecs/rt5640/DigitalMics.conf
/usr/share/alsa/ucm2/codecs/rt5640/EnableSeq.conf
/usr/share/alsa/ucm2/codecs/rt5640/HeadPhones.conf
/usr/share/alsa/ucm2/codecs/rt5640/HeadPhones2.conf
/usr/share/alsa/ucm2/codecs/rt5640/HeadsetMic.conf
/usr/share/alsa/ucm2/codecs/rt5640/HeadsetMic2-IN1.conf
/usr/share/alsa/ucm2/codecs/rt5640/IN1-InternalMic.conf
/usr/share/alsa/ucm2/codecs/rt5640/IN3-InternalMic.conf
/usr/share/alsa/ucm2/codecs/rt5640/MonoSpeaker.conf
/usr/share/alsa/ucm2/codecs/rt5640/Speaker.conf
/usr/share/alsa/ucm2/codecs/rt5640/init.conf
/usr/share/alsa/ucm2/codecs/rt5645/AnalogMic.conf
/usr/share/alsa/ucm2/codecs/rt5645/DigitalMicDisableSeq.conf
/usr/share/alsa/ucm2/codecs/rt5645/DigitalMicEnableSeq.conf
/usr/share/alsa/ucm2/codecs/rt5645/DisableSeq.conf
/usr/share/alsa/ucm2/codecs/rt5645/EnableSeq.conf
/usr/share/alsa/ucm2/codecs/rt5645/HSMicDisableSeq.conf
/usr/share/alsa/ucm2/codecs/rt5645/HSMicEnableSeq.conf
/usr/share/alsa/ucm2/codecs/rt5645/HeadphonesEnableSeq.conf
/usr/share/alsa/ucm2/codecs/rt5645/SpeakerEnableSeq.conf
/usr/share/alsa/ucm2/codecs/rt5645/init.conf
/usr/share/alsa/ucm2/codecs/rt5651/DigitalMic.conf
/usr/share/alsa/ucm2/codecs/rt5651/EnableSeq.conf
/usr/share/alsa/ucm2/codecs/rt5651/HeadPhones-swapped.conf
/usr/share/alsa/ucm2/codecs/rt5651/HeadPhones.conf
/usr/share/alsa/ucm2/codecs/rt5651/IN1-InternalMic.conf
/usr/share/alsa/ucm2/codecs/rt5651/IN12-InternalMic.conf
/usr/share/alsa/ucm2/codecs/rt5651/IN2-HeadsetMic.conf
/usr/share/alsa/ucm2/codecs/rt5651/IN2-InternalMic.conf
/usr/share/alsa/ucm2/codecs/rt5651/IN3-HeadsetMic.conf
/usr/share/alsa/ucm2/codecs/rt5651/MonoSpeaker.conf
/usr/share/alsa/ucm2/codecs/rt5651/Speaker.conf
/usr/share/alsa/ucm2/codecs/rt5651/init.conf
/usr/share/alsa/ucm2/codecs/rt5672/DMIC1.conf
/usr/share/alsa/ucm2/codecs/rt5672/DMIC2.conf
/usr/share/alsa/ucm2/codecs/rt5672/EnableSeq.conf
/usr/share/alsa/ucm2/codecs/rt5672/HeadPhones.conf
/usr/share/alsa/ucm2/codecs/rt5672/HeadsetMic.conf
/usr/share/alsa/ucm2/codecs/rt5672/MonoSpeaker.conf
/usr/share/alsa/ucm2/codecs/rt5672/Speaker.conf
/usr/share/alsa/ucm2/codecs/rt5682/init.conf
/usr/share/alsa/ucm2/codecs/rt700/init.conf
/usr/share/alsa/ucm2/codecs/rt711-sdca/init.conf
/usr/share/alsa/ucm2/codecs/rt711/init.conf
/usr/share/alsa/ucm2/codecs/rt715-sdca/init.conf
/usr/share/alsa/ucm2/codecs/rt715/init.conf
/usr/share/alsa/ucm2/codecs/wcd934x/DefaultDisableSeq.conf
/usr/share/alsa/ucm2/codecs/wcd934x/DefaultEnableSeq.conf
/usr/share/alsa/ucm2/codecs/wcd934x/HeadphoneDisableSeq.conf
/usr/share/alsa/ucm2/codecs/wcd934x/HeadphoneEnableSeq.conf
/usr/share/alsa/ucm2/codecs/wcd934x/HeadphoneMicDisableSeq.conf
/usr/share/alsa/ucm2/codecs/wcd934x/HeadphoneMicEnableSeq.conf
/usr/share/alsa/ucm2/codecs/wcd934x/SpeakerDisableSeq.conf
/usr/share/alsa/ucm2/codecs/wcd934x/SpeakerEnableSeq.conf
/usr/share/alsa/ucm2/codecs/wm5102/EnableSeq.conf
/usr/share/alsa/ucm2/codecs/wm5102/HeadPhones.conf
/usr/share/alsa/ucm2/codecs/wm5102/IN1-HeadsetMic.conf
/usr/share/alsa/ucm2/codecs/wm5102/IN3-InternalMic.conf
/usr/share/alsa/ucm2/codecs/wm5102/Speaker.conf
/usr/share/alsa/ucm2/codecs/wsa881x/DefaultEnableSeq.conf
/usr/share/alsa/ucm2/codecs/wsa881x/SpeakerDisableSeq.conf
/usr/share/alsa/ucm2/codecs/wsa881x/SpeakerEnableSeq.conf
/usr/share/alsa/ucm2/common/ctl/remap.conf
/usr/share/alsa/ucm2/common/direct-verb.conf
/usr/share/alsa/ucm2/common/direct.conf
/usr/share/alsa/ucm2/common/linked-card.conf
/usr/share/alsa/ucm2/common/linked.conf
/usr/share/alsa/ucm2/common/pcm/split.conf
/usr/share/alsa/ucm2/conf.d/DB410c/DB410c.conf
/usr/share/alsa/ucm2/conf.d/DB820c/DB820c.conf
/usr/share/alsa/ucm2/conf.d/HDA-Intel/HDA-Intel.conf
/usr/share/alsa/ucm2/conf.d/SC7180/sc7180-rt5682-max98357a-1mic.conf
/usr/share/alsa/ucm2/conf.d/SOF/SOF.conf
/usr/share/alsa/ucm2/conf.d/USB-Audio/USB-Audio.conf
/usr/share/alsa/ucm2/conf.d/VEYRON-I2S/VEYRON-I2S.conf
/usr/share/alsa/ucm2/conf.d/acp/acp.conf
/usr/share/alsa/ucm2/conf.d/acp6x/acp6x.conf
/usr/share/alsa/ucm2/conf.d/bdw-rt5677/bdw-rt5677.conf
/usr/share/alsa/ucm2/conf.d/broadwell-rt286/broadwell-rt286.conf
/usr/share/alsa/ucm2/conf.d/broxton-rt298/broxton-rt298.conf
/usr/share/alsa/ucm2/conf.d/bytcht-cx2072x/bytcht-cx2072x.conf
/usr/share/alsa/ucm2/conf.d/bytcht-es8316/bytcht-es8316.conf
/usr/share/alsa/ucm2/conf.d/bytcr-rt5640/bytcr-rt5640.conf
/usr/share/alsa/ucm2/conf.d/bytcr-rt5651/bytcr-rt5651.conf
/usr/share/alsa/ucm2/conf.d/bytcr-wm5102/bytcr-wm5102.conf
/usr/share/alsa/ucm2/conf.d/cht-bsw-rt5672/cht-bsw-rt5672.conf
/usr/share/alsa/ucm2/conf.d/chtmax98090/chtmax98090.conf
/usr/share/alsa/ucm2/conf.d/chtnau8824/chtnau8824.conf
/usr/share/alsa/ucm2/conf.d/chtrt5645/chtrt5645.conf
/usr/share/alsa/ucm2/conf.d/chtrt5650/chtrt5650.conf
/usr/share/alsa/ucm2/conf.d/hda-dsp/hda-dsp.conf
/usr/share/alsa/ucm2/conf.d/kblrt5660/kblrt5660.conf
/usr/share/alsa/ucm2/conf.d/mt8195_demo/mt8195_demo.conf
/usr/share/alsa/ucm2/conf.d/mtk-rt5650/mtk-rt5650.conf
/usr/share/alsa/ucm2/conf.d/rk3399-gru-soun/rk3399-gru-soun.conf
/usr/share/alsa/ucm2/conf.d/rockchip_es8316/rockchip_es8316.conf
/usr/share/alsa/ucm2/conf.d/sdm845/DB845c.conf
"/usr/share/alsa/ucm2/conf.d/simple-card/Librem 5 Devkit.conf"
/usr/share/alsa/ucm2/conf.d/simple-card/rockchip,es8316-codec.conf
/usr/share/alsa/ucm2/conf.d/skylake-rt286/skylake-rt286.conf
/usr/share/alsa/ucm2/conf.d/sm8250/Qualcomm-RB5-WSA8815-Speakers-DMIC0.conf
/usr/share/alsa/ucm2/conf.d/sof-ehl-rt5660/sof-ehl-rt5660.conf
/usr/share/alsa/ucm2/conf.d/sof-essx8336/sof-essx8336.conf
/usr/share/alsa/ucm2/conf.d/sof-hda-dsp/sof-hda-dsp.conf
/usr/share/alsa/ucm2/conf.d/sof-hda-dsp/sof-skl_hda_card.conf
/usr/share/alsa/ucm2/conf.d/sof-skl_hda_card
/usr/share/alsa/ucm2/conf.d/sof-soundwire/sof-soundwire.conf
/usr/share/alsa/ucm2/conf.d/tegra-hda/tegra-hda.conf
"/usr/share/alsa/ucm2/conf.d/tegra/ASUS Google Nexus 7 ALC5642.conf"
"/usr/share/alsa/ucm2/conf.d/tegra/Acer Iconia Tab A500 WM8903.conf"
"/usr/share/alsa/ucm2/conf.d/tegra/Compal PAZ00.conf"
/usr/share/alsa/ucm2/conf.d/tegra/GoogleNyanBig.conf
/usr/share/alsa/ucm2/conf.d/tegra/GoogleNyanBlaze.conf
/usr/share/alsa/ucm2/conf.virt.d/.gitignore
/usr/share/alsa/ucm2/lib/card-init.conf
/usr/share/alsa/ucm2/lib/ctl-remap.conf
/usr/share/alsa/ucm2/lib/generic.conf
/usr/share/alsa/ucm2/module/snd_soc_apq8016_sbc.conf
/usr/share/alsa/ucm2/module/snd_soc_apq8096.conf
/usr/share/alsa/ucm2/module/snd_soc_omap_abe_twl6040.conf
/usr/share/alsa/ucm2/module/snd_soc_rk3399_gru_sound.conf
/usr/share/alsa/ucm2/module/snd_soc_rockchip_max98090.conf
/usr/share/alsa/ucm2/module/snd_soc_sdm845.conf
/usr/share/alsa/ucm2/module/snd_soc_snow.conf
/usr/share/alsa/ucm2/module/snd_soc_tegra_alc5632.conf
/usr/share/alsa/ucm2/module/snd_soc_tegra_max98090.conf
/usr/share/alsa/ucm2/platforms/bytcr/PlatformDisableSeq.conf
/usr/share/alsa/ucm2/platforms/bytcr/PlatformEnableSeq.conf
/usr/share/alsa/ucm2/sof-soundwire/Hdmi.conf
/usr/share/alsa/ucm2/sof-soundwire/HiFi.conf
/usr/share/alsa/ucm2/sof-soundwire/dmic.conf
/usr/share/alsa/ucm2/sof-soundwire/rt1308-1.conf
/usr/share/alsa/ucm2/sof-soundwire/rt1308-2.conf
/usr/share/alsa/ucm2/sof-soundwire/rt1316-1.conf
/usr/share/alsa/ucm2/sof-soundwire/rt1316-2.conf
/usr/share/alsa/ucm2/sof-soundwire/rt5682.conf
/usr/share/alsa/ucm2/sof-soundwire/rt700.conf
/usr/share/alsa/ucm2/sof-soundwire/rt711-sdca.conf
/usr/share/alsa/ucm2/sof-soundwire/rt711.conf
/usr/share/alsa/ucm2/sof-soundwire/rt715-sdca.conf
/usr/share/alsa/ucm2/sof-soundwire/rt715.conf
/usr/share/alsa/ucm2/sof-soundwire/sof-soundwire.conf
/usr/share/alsa/ucm2/ucm.conf

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/alsa-ucm-conf/27f14a443d8b2c78e6684ac3bb2fee5d8364c78f
