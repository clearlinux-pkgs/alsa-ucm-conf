#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : alsa-ucm-conf
Version  : 1.2.2
Release  : 1
URL      : https://github.com/alsa-project/alsa-ucm-conf/archive/v1.2.2.tar.gz
Source0  : https://github.com/alsa-project/alsa-ucm-conf/archive/v1.2.2.tar.gz
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
%setup -q -n alsa-ucm-conf-1.2.2
cd %{_builddir}/alsa-ucm-conf-1.2.2
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583472930
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1583472930
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/alsa-ucm-conf
cp %{_builddir}/alsa-ucm-conf-1.2.2/LICENSE %{buildroot}/usr/share/package-licenses/alsa-ucm-conf/27f14a443d8b2c78e6684ac3bb2fee5d8364c78f
%make_install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/alsa/LICENSE
/usr/share/alsa/Makefile
/usr/share/alsa/README.md
/usr/share/alsa/ucm/README.md
/usr/share/alsa/ucm2/DAISY-I2S/DAISY-I2S.conf
/usr/share/alsa/ucm2/DAISY-I2S/HiFi.conf
/usr/share/alsa/ucm2/DB410c/DB410c.conf
/usr/share/alsa/ucm2/DB410c/HDMI.conf
/usr/share/alsa/ucm2/DB410c/HiFi.conf
/usr/share/alsa/ucm2/DB820c/DB820c.conf
/usr/share/alsa/ucm2/DB820c/HDMI.conf
/usr/share/alsa/ucm2/DB820c/HiFi.conf
/usr/share/alsa/ucm2/GoogleNyan/GoogleNyan.conf
/usr/share/alsa/ucm2/GoogleNyan/HiFi.conf
/usr/share/alsa/ucm2/HDA-Intel/HDAudio-DualCodecs.conf
/usr/share/alsa/ucm2/HDA-Intel/HDAudio-Gigabyte-ALC1220DualCodecs.conf
/usr/share/alsa/ucm2/HDA-Intel/HDAudio-Lenovo-DualCodecs.conf
/usr/share/alsa/ucm2/HDA-Intel/HiFi-dual.conf
/usr/share/alsa/ucm2/PAZ00/HiFi.conf
/usr/share/alsa/ucm2/PAZ00/PAZ00.conf
/usr/share/alsa/ucm2/PAZ00/Record.conf
/usr/share/alsa/ucm2/PandaBoard/FMAnalog.conf
/usr/share/alsa/ucm2/PandaBoard/HiFi.conf
/usr/share/alsa/ucm2/PandaBoard/HiFiLP.conf
/usr/share/alsa/ucm2/PandaBoard/PandaBoard.conf
/usr/share/alsa/ucm2/PandaBoard/Record.conf
/usr/share/alsa/ucm2/PandaBoard/Voice.conf
/usr/share/alsa/ucm2/PandaBoard/VoiceCall.conf
/usr/share/alsa/ucm2/PandaBoardES/FMAnalog.conf
/usr/share/alsa/ucm2/PandaBoardES/HiFi.conf
/usr/share/alsa/ucm2/PandaBoardES/HiFiLP.conf
/usr/share/alsa/ucm2/PandaBoardES/PandaBoardES.conf
/usr/share/alsa/ucm2/PandaBoardES/Record.conf
/usr/share/alsa/ucm2/PandaBoardES/Voice.conf
/usr/share/alsa/ucm2/PandaBoardES/VoiceCall.conf
/usr/share/alsa/ucm2/README.md
/usr/share/alsa/ucm2/SDP4430/FMAnalog.conf
/usr/share/alsa/ucm2/SDP4430/HiFi.conf
/usr/share/alsa/ucm2/SDP4430/HiFiLP.conf
/usr/share/alsa/ucm2/SDP4430/Record.conf
/usr/share/alsa/ucm2/SDP4430/SDP4430.conf
/usr/share/alsa/ucm2/SDP4430/Voice.conf
/usr/share/alsa/ucm2/SDP4430/VoiceCall.conf
/usr/share/alsa/ucm2/USB-Audio/Dell-WD15-Dock-HiFi.conf
/usr/share/alsa/ucm2/USB-Audio/Dell-WD15-Dock.conf
/usr/share/alsa/ucm2/VEYRON-I2S/HiFi.conf
/usr/share/alsa/ucm2/VEYRON-I2S/VEYRON-I2S.conf
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
/usr/share/alsa/ucm2/cht-bsw-rt5672/HiFi-stereo-dmic2.conf
/usr/share/alsa/ucm2/cht-bsw-rt5672/HiFi.conf
/usr/share/alsa/ucm2/cht-bsw-rt5672/LENOVO-20BN002QGE-ThinkPad8-20BN002QGE.conf
/usr/share/alsa/ucm2/cht-bsw-rt5672/LENOVO-20BN002QGE-ThinkPad8.conf
/usr/share/alsa/ucm2/cht-bsw-rt5672/cht-bsw-rt5672-stereo-dmic2.conf
/usr/share/alsa/ucm2/cht-bsw-rt5672/cht-bsw-rt5672.conf
/usr/share/alsa/ucm2/chtnau8824/HiFi-mono.conf
/usr/share/alsa/ucm2/chtnau8824/HiFi.conf
/usr/share/alsa/ucm2/chtnau8824/PIPO-W2S-Defaultstring-CherryTrailCR.conf
/usr/share/alsa/ucm2/chtnau8824/chtnau8824-mono.conf
/usr/share/alsa/ucm2/chtnau8824/chtnau8824.conf
/usr/share/alsa/ucm2/chtnau8824/cube-i1_TF-Defaultstring-CherryTrailCR.conf
/usr/share/alsa/ucm2/chtrt5645/ASUSTeKCOMPUTERINC.-T100HAN-1.0-T100HAN.conf
/usr/share/alsa/ucm2/chtrt5645/HiFi-dmic1.conf
/usr/share/alsa/ucm2/chtrt5645/HiFi-dmic2.conf
/usr/share/alsa/ucm2/chtrt5645/HiFi-mono-speaker-analog-mic.conf
/usr/share/alsa/ucm2/chtrt5645/HiFi.conf
/usr/share/alsa/ucm2/chtrt5645/LENOVO-80XF-LenovoMIIX320_10ICR-LNVNB161216.conf
/usr/share/alsa/ucm2/chtrt5645/TECLAST-X80Pro-Defaultstring-CherryTrailCR.conf
/usr/share/alsa/ucm2/chtrt5645/chtrt5645-dmic1.conf
/usr/share/alsa/ucm2/chtrt5645/chtrt5645-dmic2.conf
/usr/share/alsa/ucm2/chtrt5645/chtrt5645-mono-speaker-analog-mic.conf
/usr/share/alsa/ucm2/chtrt5645/chtrt5645.conf
/usr/share/alsa/ucm2/chtrt5645/gpd-win-pocket-rt5645.conf
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
/usr/share/alsa/ucm2/codecs/nau8824/EnableSeq.conf
/usr/share/alsa/ucm2/codecs/nau8824/HeadPhones.conf
/usr/share/alsa/ucm2/codecs/nau8824/HeadsetMic.conf
/usr/share/alsa/ucm2/codecs/nau8824/InternalMic.conf
/usr/share/alsa/ucm2/codecs/nau8824/MonoSpeaker.conf
/usr/share/alsa/ucm2/codecs/nau8824/Speaker.conf
/usr/share/alsa/ucm2/codecs/rt5640/DigitalMics.conf
/usr/share/alsa/ucm2/codecs/rt5640/EnableSeq.conf
/usr/share/alsa/ucm2/codecs/rt5640/HeadPhones.conf
/usr/share/alsa/ucm2/codecs/rt5640/HeadsetMic.conf
/usr/share/alsa/ucm2/codecs/rt5640/IN1-InternalMic.conf
/usr/share/alsa/ucm2/codecs/rt5640/IN3-InternalMic.conf
/usr/share/alsa/ucm2/codecs/rt5640/MonoSpeaker.conf
/usr/share/alsa/ucm2/codecs/rt5640/Speaker.conf
/usr/share/alsa/ucm2/codecs/rt5645/AnalogMic.conf
/usr/share/alsa/ucm2/codecs/rt5645/DigitalMicDisableSeq.conf
/usr/share/alsa/ucm2/codecs/rt5645/DigitalMicEnableSeq.conf
/usr/share/alsa/ucm2/codecs/rt5645/DisableSeq.conf
/usr/share/alsa/ucm2/codecs/rt5645/EnableSeq.conf
/usr/share/alsa/ucm2/codecs/rt5645/HSMicDisableSeq.conf
/usr/share/alsa/ucm2/codecs/rt5645/HSMicEnableSeq.conf
/usr/share/alsa/ucm2/codecs/rt5645/HeadphonesEnableSeq.conf
/usr/share/alsa/ucm2/codecs/rt5645/SpeakerEnableSeq.conf
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
/usr/share/alsa/ucm2/codecs/rt5672/DMIC1.conf
/usr/share/alsa/ucm2/codecs/rt5672/DMIC2.conf
/usr/share/alsa/ucm2/codecs/rt5672/EnableSeq.conf
/usr/share/alsa/ucm2/codecs/rt5672/HeadPhones.conf
/usr/share/alsa/ucm2/codecs/rt5672/HeadsetMic.conf
/usr/share/alsa/ucm2/codecs/rt5672/MonoSpeaker.conf
/usr/share/alsa/ucm2/codecs/rt5672/Speaker.conf
/usr/share/alsa/ucm2/kblrt5660/Hdmi1.conf
/usr/share/alsa/ucm2/kblrt5660/Hdmi2.conf
/usr/share/alsa/ucm2/kblrt5660/HiFi.conf
/usr/share/alsa/ucm2/kblrt5660/kblrt5660.conf
/usr/share/alsa/ucm2/platforms/bytcr/PlatformDisableSeq.conf
/usr/share/alsa/ucm2/platforms/bytcr/PlatformEnableSeq.conf
/usr/share/alsa/ucm2/skylake-rt286/Hdmi1.conf
/usr/share/alsa/ucm2/skylake-rt286/Hdmi2.conf
/usr/share/alsa/ucm2/skylake-rt286/HiFi.conf
/usr/share/alsa/ucm2/skylake-rt286/skylake-rt286.conf
/usr/share/alsa/ucm2/sof-hda-dsp/HDA-Capture-value.conf
/usr/share/alsa/ucm2/sof-hda-dsp/Hdmi.conf
/usr/share/alsa/ucm2/sof-hda-dsp/HiFi.conf
/usr/share/alsa/ucm2/sof-hda-dsp/sof-hda-dsp.conf
/usr/share/alsa/ucm2/tegraalc5632/tegraalc5632.conf

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/alsa-ucm-conf/27f14a443d8b2c78e6684ac3bb2fee5d8364c78f
