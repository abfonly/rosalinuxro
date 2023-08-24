%define git 8806dd0
%define _disable_ld_no_undefined 1
%define _disable_ld_as_needed 1
%define Werror_cflags -Wformat

%define oname cinelerra
%define distsuffix mrb
%define snap 20230331


Summary:	Non-Linear Video Editing Suite
Name:		cinelerra-gg
Version:	5.1
Release:	%{snap}.1
License:	GPLv2+
Group:		Video
Url:		https://www.cinelerra-gg.org/
Source0:	https://cinelerra-gg.org/download/pkgs/src/cin_%{version}.%{snap}-src.tgz
Source1:	cinx.appdata.xml
Source2:	https://cinelerra-gg.org/download/releasenotes_last.pdf
Source3:	https://cinelerra-gg.org/download/CinelerraGG_Manual.pdf 
Source4:	https://cinelerra-gg.org/download/CinelerraGG_Quickstart.pdf
Source100:	%{name}.rpmlintrc

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cmake
BuildRequires:	binutils
BuildRequires:	ctags
BuildRequires:	flac-devel
BuildRequires:	gcc-c++
BuildRequires:	gettext-devel
BuildRequires:	git
BuildRequires:	inkscape
BuildRequires:	imagemagick
BuildRequires:	libtool
BuildRequires:	nasm
BuildRequires:	texinfo
BuildRequires:	yasm
BuildRequires:	a52dec-devel
BuildRequires:	jpeg-devel
BuildRequires:	libfaac-devel
BuildRequires:	pkgconfig(faad2)
# provides to be fixed in main
%ifarch x86_64
BuildRequires:	devel(libmp4v2(64bit))
BuildRequires:	nvidia-cuda-toolkit-devel
BuildRequires:	nvidia-devel
%else
BuildRequires:	devel(libmp4v2)
%endif
BuildRequires:	xvid-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(libffi)
BuildRequires:	pkgconfig(libglvnd)
BuildRequires:	pkgconfig(audiofile)
BuildRequires:	pkgconfig(esound)
BuildRequires:	pkgconfig(ext2fs)
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
# conflict with openexr3 
# BuildRequires:	pkgconfig(IlmBase)
BuildRequires:	pkgconfig(libavc1394)
BuildRequires:	pkgconfig(libdv)
BuildRequires:	pkgconfig(libiec61883)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libraw1394)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(mjpegtools)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(ogg)
BuildRequires:	pkgconfig(OpenEXR)
BuildRequires:	openexr-utils
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(theora)
BuildRequires:	pkgconfig(uuid)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(x264)
BuildRequires:	pkgconfig(x265)
BuildRequires:	fltk-devel
BuildRequires:	pkgconfig(libthai)
BuildRequires:	pkgconfig(opencv)
BuildRequires:	pkgconfig(xv)
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(imlib2)
BuildRequires:	libamrwb-devel
BuildRequires:	libamrnb-devel
BuildRequires:	pkgconfig(libdc1394-2)
BuildRequires:	pkgconfig(dirac)
BuildRequires:	pkgconfig(schroedinger-1.0)
BuildRequires:	libnut-devel
BuildRequires:	gsm-devel
BuildRequires:	a52dec-devel
BuildRequires:	docbook2x
BuildRequires:	pkgconfig(xxf86vm)
BuildRequires:	pkgconfig(xft)
BuildRequires:	pkgconfig(twolame)
BuildRequires:	pkgconfig(vdpau)
BuildRequires:	pkgconfig(audiofile)
BuildRequires:	pkgconfig(esound)
BuildRequires:	pkgconfig(numa)
BuildRequires:	pkgconfig(fdk-aac)
BuildRequires:	pkgconfig(harfbuzz)
BuildRequires:	pkgconfig(datrie-0.2)
BuildRequires:	desktop-file-utils
BuildRequires:	lame-devel
BuildRequires:	lame-static-devel
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	gtk+2.0
BuildRequires:	pkgconfig(lcms)
BuildRequires:	pkgconfig(lcms2)
BuildRequires:	pkgconfig(lilv-0)
BuildRequires:	pkgconfig(dav1d)
BuildRequires:	pkgconfig(sord-0)
BuildRequires:	pkgconfig(serd-0)
BuildRequires:	pkgconfig(sratom-0)
BuildRequires:	pkgconfig(Imath)
BuildRequires:	pkgconfig(libisofs-1)
BuildRequires:	pkgconfig(suil-0)
BuildRequires:	pkgconfig(vulkan)
BuildRequires:	vulkan-intel-devel
BuildRequires:	vulkan-headers
BuildRequires:	vulkan-tools



Requires:	%{name}-plugins = %{EVRD}

Obsoletes:  cinelerra < %{EVRD}
Conflicts:	cinelerra-cv
# arm not suported sse instructions
ExclusiveArch:	x86_64 %{ix86}


%description
If you want to make movies, you want the compositing and editing that
the big boys use, you want the efficiency of an embedded UNIX operating
system combined with the power of a general purpose PC, or you just want
to defy the establishment, the time has come to download Cinelerra.

This version is based on the "Community" tree found at
http://cinelerra-cv.org.

This package is in restricted because MP3 encoder and video codecs are
covered by software patents.

%files -f cinx.lang
%doc doc/ *.pdf
%{_bindir}/*
%exclude %{_libdir}/cinx/plugins
%{_libdir}/cinx/
%{_datadir}/applications/*.desktop
%{_datadir}/cinx/
%{_iconsdir}/hicolor/*/apps/cinx.png
%{_iconsdir}/hicolor/scalable/cinx.svg
%{_appdatadir}/*.appdata.xml
#----------------------------------------------------------------------------
%package	plugins
Summary:        Plugins for GG
Group:          System/Libraries

%description	plugins
Plugins for cinelerra-gg

%files		plugins
%doc README COPYING
%{_libdir}/cinx/plugins

#------------------------------------------------------------------------------
%prep
%autosetup -n %{oname}-%{version}
# delete android app
rm -fr CineRmt

cp -pr %{SOURCE2} releasenotes.pdf
cp -pr %{SOURCE3} CinelerraGG_manual.pdf
cp -pr %{SOURCE4} CinelerraGG_Quickstart.pdf

chmod -x doc/*
chmod -x Cinelerra_factory
sh autogen.sh


%build
export CXXFLAGS="%{optflags} $(pkg-config --cflags freetype2) -D__STDC_CONSTANT_MACROS"
export CFLAGS="%{optflags} -fPIC"
export FFMPEG_EXTRA_CFG=" --disable-vdpau"


%ifarch x86_64 
./configure \
  --prefix=/usr \
  --with-exec-name=cinx \
  --disable-static-build \
  --enable-x264_hidepth \
  --enable-x265_hidepth
%else
./configure \
  --prefix=/usr \
  --with-exec-name=cinx \
  --disable-static-build 
%endif
%make



%install
%makeinstall_std

install -d 755 %{buildroot}%{_iconsdir}/hicolor/scalable
cp -R image/cin.svg %{buildroot}%{_iconsdir}/hicolor/scalable/cinx.svg

for size in 256x256 128x128 96x96 64x64 48x48 32x32 22x22 16x16 ; do
    install -dm 0755 \
        %{buildroot}%{_iconsdir}/hicolor/$size/apps
    convert -strip -resize $size image/cin.svg \
        %{buildroot}%{_iconsdir}/hicolor/$size/apps/cinx.png
done


rm -fr %{buildroot}%{_datadir}/pixmaps


# linting
find %{buildroot}%{_datadir}/cinx/* -type f -exec chmod 644 {} \;
find %{buildroot}%{_datadir}/cinx/*/ -type f -exec chmod 644 {} \;
chmod 644 %{buildroot}%{_datadir}/applications/cinx.desktop
chmod 644 %{buildroot}%{_datadir}/cinx/doc/*
chmod 644 %{buildroot}%{_libdir}/cinx/plugins/fonts/*

#appdata
mkdir -p %{buildroot}%{_appdatadir}
cp -pr %{SOURCE1} %{buildroot}%{_appdatadir}/cinx.appdata.xml

# remove warning
desktop-file-edit --remove-key=Encoding \
    %{buildroot}%{_datadir}/applications/cinx.desktop


%find_lang cinx


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/cinx.desktop

