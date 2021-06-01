#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x8380596DA6E59C91 (release@alsa-project.org)
#
Name     : alsa-ucm-conf
Version  : 1.2.5
Release  : 6
URL      : https://www.alsa-project.org/files/pub/lib/alsa-ucm-conf-1.2.5.tar.bz2
Source0  : https://www.alsa-project.org/files/pub/lib/alsa-ucm-conf-1.2.5.tar.bz2
Source1  : https://www.alsa-project.org/files/pub/lib/alsa-ucm-conf-1.2.5.tar.bz2.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: alsa-ucm-conf-data = %{version}-%{release}
Requires: alsa-ucm-conf-license = %{version}-%{release}
Patch1: 0001-Add-Makefile-to-make-packaging-ucm2-easier.patch

%description
# alsa-ucm-conf
## ALSA Use Case Manager configuration
![Validate UCM configuration](https://github.com/alsa-project/alsa-ucm-conf/workflows/Validate%20UCM%20configuration/badge.svg?branch=master)

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
%setup -q -n alsa-ucm-conf-1.2.4.81.g4884e
cd %{_builddir}/alsa-ucm-conf-1.2.4.81.g4884e
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1622567016
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1622567016
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/alsa-ucm-conf
cp %{_builddir}/alsa-ucm-conf-1.2.4.81.g4884e/LICENSE %{buildroot}/usr/share/package-licenses/alsa-ucm-conf/27f14a443d8b2c78e6684ac3bb2fee5d8364c78f
%make_install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/alsa/ucm2/HDA-Intel/HDA-Capture-value.conf
/usr/share/alsa/ucm2/HDA-Intel/HDA-Intel.conf
/usr/share/alsa/ucm2/HDA-Intel/HDAudio-DualCodecs.conf
/usr/share/alsa/ucm2/HDA-Intel/HDAudio-Gigabyte-ALC1220DualCodecs.conf
/usr/share/alsa/ucm2/HDA-Intel/HDAudio-Lenovo-DualCodecs.conf
/usr/share/alsa/ucm2/HDA-Intel/Hdmi.conf
/usr/share/alsa/ucm2/HDA-Intel/HiFi-acp.conf
/usr/share/alsa/ucm2/HDA-Intel/HiFi-analog.conf
/usr/share/alsa/ucm2/HDA-Intel/HiFi-dual.conf
/usr/share/alsa/ucm2/HDA-Intel/HiFi.conf
/usr/share/alsa/ucm2/HDA-Intel/init.conf
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
/usr/share/alsa/ucm2/Qualcomm/sdm845/HDMI.conf
/usr/share/alsa/ucm2/Qualcomm/sdm845/HiFi.conf
/usr/share/alsa/ucm2/Qualcomm/sdm845/sdm845.conf
/usr/share/alsa/ucm2/Qualcomm/sm8250/HDMI.conf
/usr/share/alsa/ucm2/Qualcomm/sm8250/HiFi.conf
/usr/share/alsa/ucm2/Qualcomm/sm8250/Qualcomm-RB5-WSA8815-Speakers-DMIC0.conf
/usr/share/alsa/ucm2/README.md
/usr/share/alsa/ucm2/Rockchip/max98090/HiFi.conf
/usr/share/alsa/ucm2/Rockchip/max98090/max98090.conf
/usr/share/alsa/ucm2/Rockchip/rk3399-gru-sound/HiFi.conf
/usr/share/alsa/ucm2/Rockchip/rk3399-gru-sound/rk3399-gru-sound.conf
/usr/share/alsa/ucm2/SOF/HiFi.conf
/usr/share/alsa/ucm2/SOF/SOF.conf
/usr/share/alsa/ucm2/Samsung/snow/HiFi.conf
/usr/share/alsa/ucm2/Samsung/snow/snow.conf
/usr/share/alsa/ucm2/Tegra/alc5632/HiFi.conf
/usr/share/alsa/ucm2/Tegra/alc5632/Record.conf
/usr/share/alsa/ucm2/Tegra/alc5632/alc5632.conf
/usr/share/alsa/ucm2/Tegra/max98090/HiFi.conf
/usr/share/alsa/ucm2/Tegra/max98090/max98090.conf
"/usr/share/alsa/ucm2/Tegra/rt5640/ASUS Google Nexus 7 ALC5642.conf"
"/usr/share/alsa/ucm2/Tegra/wm8903/Acer Iconia Tab A500 WM8903.conf"
/usr/share/alsa/ucm2/USB-Audio/Dell-WD15-Dock-HiFi.conf
/usr/share/alsa/ucm2/USB-Audio/Dell-WD15-Dock.conf
/usr/share/alsa/ucm2/USB-Audio/Gigabyte-Aorus-Master-Front-Headphone.conf
/usr/share/alsa/ucm2/USB-Audio/Gigabyte-Aorus-Master-Main-Audio-HiFi.conf
/usr/share/alsa/ucm2/USB-Audio/Gigabyte-Aorus-Master-Main-Audio.conf
/usr/share/alsa/ucm2/USB-Audio/Lenovo-ThinkStation-P620-Main-HiFi.conf
/usr/share/alsa/ucm2/USB-Audio/Lenovo-ThinkStation-P620-Main.conf
/usr/share/alsa/ucm2/USB-Audio/Lenovo-ThinkStation-P620-Rear-HiFi.conf
/usr/share/alsa/ucm2/USB-Audio/Lenovo-ThinkStation-P620-Rear.conf
/usr/share/alsa/ucm2/USB-Audio/Realtek-ALC1220-VB-Desktop-HiFi.conf
/usr/share/alsa/ucm2/USB-Audio/Realtek-ALC1220-VB-Desktop.conf
/usr/share/alsa/ucm2/bdw-rt5677/HiFi.conf
/usr/share/alsa/ucm2/bdw-rt5677/bdw-rt5677.conf
/usr/share/alsa/ucm2/broadwell-rt286/HiFi.conf
/usr/share/alsa/ucm2/broadwell-rt286/broadwell-rt286.conf
/usr/share/alsa/ucm2/broxton-rt298/Hdmi.conf
/usr/share/alsa/ucm2/broxton-rt298/HiFi.conf
/usr/share/alsa/ucm2/broxton-rt298/broxton-rt298.conf
/usr/share/alsa/ucm2/bytcht-cx2072x/HiFi.conf
/usr/share/alsa/ucm2/bytcht-cx2072x/bytcht-cx2072x.conf
/usr/share/alsa/ucm2/bytcht-es8316/HiFi-Components.conf
/usr/share/alsa/ucm2/bytcht-es8316/HiFi-LongName.conf
/usr/share/alsa/ucm2/bytcht-es8316/HiFi.conf
/usr/share/alsa/ucm2/bytcht-es8316/bytcht-es8316.conf
/usr/share/alsa/ucm2/bytcr-rt5640/HiFi-Components.conf
/usr/share/alsa/ucm2/bytcr-rt5640/HiFi-LongName.conf
/usr/share/alsa/ucm2/bytcr-rt5640/HiFi.conf
/usr/share/alsa/ucm2/bytcr-rt5640/bytcr-rt5640.conf
/usr/share/alsa/ucm2/bytcr-rt5651/HiFi-Components.conf
/usr/share/alsa/ucm2/bytcr-rt5651/HiFi-LongName.conf
/usr/share/alsa/ucm2/bytcr-rt5651/HiFi.conf
/usr/share/alsa/ucm2/bytcr-rt5651/bytcr-rt5651.conf
/usr/share/alsa/ucm2/bytcr-wm5102/HiFi.conf
/usr/share/alsa/ucm2/bytcr-wm5102/bytcr-wm5102.conf
/usr/share/alsa/ucm2/cht-bsw-rt5672/HiFi.conf
/usr/share/alsa/ucm2/cht-bsw-rt5672/cht-bsw-rt5672.conf
/usr/share/alsa/ucm2/chtmax98090/HiFi.conf
/usr/share/alsa/ucm2/chtmax98090/chtmax98090.conf
/usr/share/alsa/ucm2/chtnau8824/HiFi.conf
/usr/share/alsa/ucm2/chtnau8824/chtnau8824.conf
/usr/share/alsa/ucm2/chtrt5645/HiFi.conf
/usr/share/alsa/ucm2/chtrt5645/chtrt5645.conf
/usr/share/alsa/ucm2/chtrt5650/HiFi.conf
/usr/share/alsa/ucm2/chtrt5650/chtrt5650.conf
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
/usr/share/alsa/ucm2/codecs/rt5640/HeadsetMic.conf
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
/usr/share/alsa/ucm2/conf.d/DB410c/DB410c.conf
/usr/share/alsa/ucm2/conf.d/DB820c/DB820c.conf
/usr/share/alsa/ucm2/conf.d/sdm845/DB845c.conf
/usr/share/alsa/ucm2/conf.d/sm8250/Qualcomm-RB5-WSA8815-Speakers-DMIC0.conf
"/usr/share/alsa/ucm2/conf.d/tegra/ASUS Google Nexus 7 ALC5642.conf"
"/usr/share/alsa/ucm2/conf.d/tegra/Acer Iconia Tab A500 WM8903.conf"
"/usr/share/alsa/ucm2/conf.d/tegra/Compal PAZ00.conf"
/usr/share/alsa/ucm2/conf.d/tegra/GoogleNyanBig.conf
/usr/share/alsa/ucm2/conf.d/tegra/GoogleNyanBlaze.conf
/usr/share/alsa/ucm2/conf.virt.d/.gitignore
/usr/share/alsa/ucm2/hda-dsp/Hdmi1.conf
/usr/share/alsa/ucm2/hda-dsp/Hdmi2.conf
/usr/share/alsa/ucm2/hda-dsp/HiFi.conf
/usr/share/alsa/ucm2/hda-dsp/hda-dsp.conf
/usr/share/alsa/ucm2/kblrt5660/Hdmi1.conf
/usr/share/alsa/ucm2/kblrt5660/Hdmi2.conf
/usr/share/alsa/ucm2/kblrt5660/HiFi.conf
/usr/share/alsa/ucm2/kblrt5660/kblrt5660.conf
/usr/share/alsa/ucm2/lib/card-init.conf
/usr/share/alsa/ucm2/lib/ctl-remap.conf
/usr/share/alsa/ucm2/lib/generic.conf
/usr/share/alsa/ucm2/module/lib/linked.conf
/usr/share/alsa/ucm2/module/snd_acp3x_rn.conf
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
/usr/share/alsa/ucm2/skylake-rt286/Hdmi1.conf
/usr/share/alsa/ucm2/skylake-rt286/Hdmi2.conf
/usr/share/alsa/ucm2/skylake-rt286/HiFi.conf
/usr/share/alsa/ucm2/skylake-rt286/skylake-rt286.conf
/usr/share/alsa/ucm2/sof-hda-dsp/Hdmi.conf
/usr/share/alsa/ucm2/sof-hda-dsp/HiFi.conf
/usr/share/alsa/ucm2/sof-hda-dsp/sof-hda-dsp.conf
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
