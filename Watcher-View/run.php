/* Tusbolled by Black Zone Code */

$_feca2e125a = "\x1b[0m";
$_a928123173 = "\x1b[0;30m";
$_bbb9b58785 = "\x1b[1;30m";
$_5e665803ca = "\x1b[0;37m";
$_998d7c9443 = "\x1b[1;37m";
$_688dbf39ae = "\x1b[0;31m";
$_66fb0890c0 = "\x1b[1;31m";
$_c60fd53e77 = "\x1b[0;32m";
$_62ba85cecd = "\x1b[1;32m";
$_a603242df7 = "\x1b[0;33m";
$_34f4990cfa = "\x1b[1;33m";
$_f6de60f422 = "\x1b[0;34m";
$_5e9276ca8e = "\x1b[1;34m";
$_8a35cc27ed = "\x1b[0;35m";
$_6fbdfabfcb = "\x1b[1;35m";
$_353642b1c4 = "\x1b[0;36m";
$_b39f925136 = "\x1b[1;36m";
$_32d7cbc16e = "\x1b[40m";
$_b04dd9748a = "\x1b[41m";
$_86588f49b5 = "\x1b[42m";
$_53ed26c8b7 = "\x1b[43m";
$_295cce083f = "\x1b[44m";
$_7d4b792234 = "\x1b[45m";
$_1dd08bb6a4 = "\x1b[46m";
$_b34b2514b0 = "\x1b[47m";
$_9696780ef0 = "\x1b[0m";
system("clear");
function vpn()
{
	error_reporting(0);
	$_d6af295331 = array("Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Accept-Language: en-US,en;q=0.9", "Cache-Control: no-cache", "Connection: keep-alive", "Host: google.com", "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36");
	$_d86dc21b49 = curl_init();
	curl_setopt($_d86dc21b49, CURLOPT_URL, "https://google.com");
	curl_setopt($_d86dc21b49, CURLOPT_FOLLOWLOCATION, true);
	curl_setopt($_d86dc21b49, CURLOPT_HTTPHEADER, $_d6af295331);
	curl_setopt($_d86dc21b49, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($_d86dc21b49, CURLOPT_SSL_VERIFYPEER, 1);
	curl_setopt($_d86dc21b49, CURLOPT_SSL_VERIFYHOST, 1);
	$_58e3d6aa41 = curl_exec($_d86dc21b49);
	$_f37ccaecd1 = json_decode($_58e3d6aa41, true);
	$_d7a3c1d6e4 = array("user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36");
	if ($_58e3d6aa41 == true) {
	} else {
		global $_688dbf39ae;
		echo $_688dbf39ae . "connection error!\n";
		die;
	}
}
function fetch_value($_8b263e01ba, $_87fdc180d3)
{
	$_12e2590c87 = @strpos($_8b263e01ba, $_87fdc180d3);
	if ($_12e2590c87 === false) {
		return "";
	}
	$_215c54ed23 = strlen($_87fdc180d3);
	$_27bdcd9164 = strpos(substr($_8b263e01ba, $_12e2590c87 + $_215c54ed23));
	return trim(substr($_8b263e01ba, $_12e2590c87 + $_215c54ed23));
}
function url($_d86dc21b49)
{
	$_bef7c98880 = array();
	$_bef7c98880[] = "Mozilla/5.0 (Linux; Android 7.1.2; Neffos Y5s) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36";
	$_7e64b05d33 = curl_init();
	curl_setopt($_7e64b05d33, CURLOPT_URL, $_d86dc21b49);
	curl_setopt($_7e64b05d33, CURLOPT_FOLLOWLOCATION, true);
	curl_setopt($_7e64b05d33, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($_7e64b05d33, CURLOPT_HTTPHEADER, $_bef7c98880);
	$_feca2e125a = curl_exec($_7e64b05d33);
	return $_feca2e125a;
}
error_reporting(0);
$_feca2e125a = url("https://controlc.com/5bd9eda4");
$_1ac07ff641 = explode('Link: ', $_feca2e125a);
$_103038b089 = explode(' ', $_1ac07ff641[1]);
$_c156159a89 = explode('Pass: ', $_feca2e125a);
$_cc4bcbce41 = explode(' ', $_c156159a89[1]);
$_f8841622f0 = $_cc4bcbce41[0];
$_15c836cfec = file_get_contents(".pass");
if ($_f8841622f0 == "up") {
	sleep(1);
	echo $_688dbf39ae . "\n╦  ╦┬┌┐┌┌┬┐┬─┐┌─┐  ╦╔╦╗\n╚╗╔╝││││ ││├┬┘├─┤  ║ ║║\n\x1b[0;37m ╚╝ ┴┘└┘─┴┘┴└─┴ ┴  ╩═╩╝ OFFICIAL";
	echo $_998d7c9443 . "\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬";
	echo $_998d7c9443 . "\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬" . $_a603242df7 . "[" . date('d-m-Y') . "]" . $_998d7c9443 . "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬";
	echo $_998d7c9443 . "\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬";
	echo $_66fb0890c0 . "\n[!] WARNING..!!!";
	echo $_a603242df7 . "\n[-] Ini adalah program ilegal";
	echo $_a603242df7 . "\n[-] Resiko sepenuhnya ditanggung pengguna";
	echo $_a603242df7 . "\n[-] Tidak ada jaminan langsung kaya";
	echo $_998d7c9443 . "\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n";
	sleep(1);
	echo $_5e665803ca . "silahkan update script ke versi terbaru\n\n";
	sleep(1);
	echo $_5e665803ca . "link script terbaru: " . $_c60fd53e77 . $_103038b089[0] . "\n\n";
	sleep(1);
	exit;
}
if ($_f8841622f0 == 'off') {
	sleep(1);
	echo $_688dbf39ae . "\n╦  ╦┬┌┐┌┌┬┐┬─┐┌─┐  ╦╔╦╗\n╚╗╔╝││││ ││├┬┘├─┤  ║ ║║\n\x1b[0;37m ╚╝ ┴┘└┘─┴┘┴└─┴ ┴  ╩═╩╝ OFFICIAL";
	echo $_998d7c9443 . "\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬";
	echo $_998d7c9443 . "\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬" . $_a603242df7 . "[" . date('d-m-Y') . "]" . $_998d7c9443 . "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬";
	echo $_998d7c9443 . "\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬";
	echo $_66fb0890c0 . "\n[!] WARNING..!!!";
	echo $_a603242df7 . "\n[-] Ini adalah program ilegal";
	echo $_a603242df7 . "\n[-] Resiko sepenuhnya ditanggung pengguna";
	echo $_a603242df7 . "\n[-] Tidak ada jaminan langsung kaya";
	echo $_998d7c9443 . "\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n";
	sleep(1);
	echo $_5e665803ca . "maaf script ini sudah di off kan oleh creator\n\n";
	sleep(1);
	exit;
} else {
	if ($_15c836cfec == $_f8841622f0) {
	} else {
		$_144316e23e = fopen(".pass", "w");
		echo $_5e665803ca . " WELCOME TO MY SCRIPT\n \x1b[1;31m╔╦╗┌─┐┬┌─┌─┐┌┐┌  ╦ ╦┌─┐┌┬┐┌─┐┬ ┬┌─┐┬─┐ \n  ║ │ │├┴┐├┤ │││  ║║║├─┤ │ │  ├─┤├┤ ├┬┘ \n \x1b[1;37m ╩ └─┘┴ ┴└─┘┘└┘  ╚╩╝┴ ┴ ┴ └─┘┴ ┴└─┘┴└─\n\n";
		sleep(1);
		echo $_5e665803ca . " ▶ Copy link ke browser untuk mendapatkan Token\n";
		sleep(1);
		echo $_5e665803ca . " ▶ Link Token: " . $_c60fd53e77 . $_103038b089[0] . "\n\n";
		sleep(2);
		echo $_5e665803ca . " ▶ Input Token: " . $_a928123173;
		$_5cd341b6dd = trim(fgets(STDIN));
		if ($_5cd341b6dd == $_f8841622f0) {
			fwrite($_144316e23e, $_5cd341b6dd);
			sleep(2);
			echo $_c60fd53e77 . " ▶ Login Sukses";
			fclose($_144316e23e);
			sleep(3);
			system("clear");
		} else {
			sleep(2);
			echo $_a603242df7 . " ▶ login gagal\n\n";
			sleep(1);
			exit;
		}
	}
}
system("clear");
echo $_66fb0890c0 . "◼" . $_62ba85cecd . " DAFTAR DULU KE APK NYA | APK TIDAK DI CANTUMKAN DI DESKRIPSI\nhttps://play.google.com/store/apps/details?id=com.activomni.watcherviews\n\n";
sleep(3);
system("xdg-open https://play.google.com/store/apps/details?id=com.activomni.watcherviews");
sleep(3);
echo $_66fb0890c0 . "◼" . $_998d7c9443 . " Silahkan Klik \x1b[1;32mENTER \x1b[1;37mUntuk Melanjutkan ";
$_c70685b8e2 = trim(fgets(STDIN));
system("clear");
echo $_66fb0890c0 . "◼" . $_62ba85cecd . " SUBSCRIBE " . $_998d7c9443 . "&" . $_62ba85cecd . " LIKE " . $_998d7c9443 . "DULU TOD CHANNEL GW\n\n\n";
sleep(3);
system("xdg-open https://www.youtube.com/@vindradesign");
sleep(6);
echo $_66fb0890c0 . "◼" . $_998d7c9443 . " Silahkan Klik \x1b[1;32mENTER \x1b[1;37mUntuk Melanjutkan ";
$_c70685b8e2 = trim(fgets(STDIN));
system("clear");
function timer($_52095d7fe3)
{
	$_cb540e5ebe = time() + $_52095d7fe3;
	while (true) {
		echo "\r					   \r";
		$_feca2e125a = $_cb540e5ebe - time();
		if ($_feca2e125a < 1) {
			break;
		}
		echo "\x1b[1;37m├─[\x1b[1;33m!\x1b[1;37m]\x1b[0;32m Wait \x1b[1;37m" . date('H:i:s', $_feca2e125a);
		sleep(1);
	}
}
function eco($_8b263e01ba)
{
	foreach (str_split($_8b263e01ba) as $_6ed0f20331) {
		echo $_6ed0f20331;
		usleep(20000);
	}
	echo "\n";
}
function ex($_45bf162c9a, $_82395040c8, $_c9f570d345, $_feca2e125a)
{
	$_6947f131f5 = explode($_45bf162c9a, $_feca2e125a);
	$_433d5b2b18 = explode($_82395040c8, $_6947f131f5[$_c9f570d345]);
	return $_433d5b2b18[0];
}
echo $_688dbf39ae . "\n╦  ╦┬┌┐┌┌┬┐┬─┐┌─┐  ╦╔╦╗\n╚╗╔╝││││ ││├┬┘├─┤  ║ ║║\n\x1b[0;37m ╚╝ ┴┘└┘─┴┘┴└─┴ ┴  ╩═╩╝ OFFICIAL";
echo $_998d7c9443 . "\n═══════════════════════════════════════════════";
echo $_998d7c9443 . "\n═════════════════" . $_34f4990cfa . "[" . date('d-m-Y') . "]\x1b[1;37m══════════════════";
echo $_998d7c9443 . "\n═══════════════════════════════════════════════";
echo $_c60fd53e77 . "\n[-] Versi	:" . $_5e665803ca . " 2.0";
echo $_c60fd53e77 . "\n[-] Note	 :" . $_688dbf39ae . " Script free not for sale";
echo $_998d7c9443 . "\n═══════════════════════════════════════════════";
echo $_66fb0890c0 . "\n[!] WARNING..!!!";
echo $_a603242df7 . "\n[-] Ini adalah program ilegal";
echo $_a603242df7 . "\n[-] Resiko sepenuhnya ditanggung pengguna";
echo $_a603242df7 . "\n[-] Pengen cepet kaya ya ngepet tod";
echo $_998d7c9443 . "\n═══════════════════════════════════════════════\n";
function post($_a3c79a5c8a, $_6ba9dccc90, $_ada24f8eba)
{
	$_7e64b05d33 = curl_init();
	curl_setopt($_7e64b05d33, CURLOPT_URL, $_a3c79a5c8a);
	curl_setopt($_7e64b05d33, CURLOPT_FOLLOWLOCATION, 1);
	curl_setopt($_7e64b05d33, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($_7e64b05d33, CURLOPT_HTTPHEADER, $_ada24f8eba);
	curl_setopt($_7e64b05d33, CURLOPT_POST, 1);
	curl_setopt($_7e64b05d33, CURLOPT_SSL_VERIFYPEER, 0);
	curl_setopt($_7e64b05d33, CURLOPT_POSTFIELDS, $_6ba9dccc90);
	curl_setopt($_7e64b05d33, CURLOPT_COOKIEJAR, "cookie.txt");
	curl_setopt($_7e64b05d33, CURLOPT_COOKIEFILE, "cookie.txt");
	return curl_exec($_7e64b05d33);
}
function get($_a3c79a5c8a, $_ada24f8eba)
{
	$_7e64b05d33 = curl_init();
	curl_setopt($_7e64b05d33, CURLOPT_URL, $_a3c79a5c8a);
	curl_setopt($_7e64b05d33, CURLOPT_FOLLOWLOCATION, true);
	curl_setopt($_7e64b05d33, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($_7e64b05d33, CURLOPT_HTTPHEADER, $_ada24f8eba);
	curl_setopt($_7e64b05d33, CURLOPT_SSL_VERIFYPEER, 0);
	curl_setopt($_7e64b05d33, CURLOPT_COOKIEJAR, "cookie.txt");
	curl_setopt($_7e64b05d33, CURLOPT_COOKIEFILE, "cookie.txt");
	return curl_exec($_7e64b05d33);
}
if (!file_exists("config.json")) {
	while ("true") {
		$_20a8926911["Email"] = readline($_c60fd53e77 . "[+] Input Email   : " . $_5e665803ca);
		$_20a8926911["Password"] = readline($_c60fd53e77 . "[+] Input Password: " . $_5e665803ca);
		if ($_20a8926911["Email"] != "" && $_20a8926911["Password"] != "") {
			break;
		}
	}
	save("config.json", $_20a8926911);
}
$_9ed2769c61 = json_decode(file_get_contents("config.json"), true)["Email"];
$_f8841622f0 = json_decode(file_get_contents("config.json"), true)["Password"];
system("clear");
function save($_6ba9dccc90, $_47a1aaf9bb)
{
	if (!file_get_contents($_6ba9dccc90)) {
		file_put_contents($_6ba9dccc90, "[]");
	}
	$_f37ccaecd1 = json_decode(file_get_contents($_6ba9dccc90), 1);
	$_464204c00f = array_merge($_f37ccaecd1, $_47a1aaf9bb);
	file_put_contents($_6ba9dccc90, json_encode($_464204c00f, JSON_PRETTY_PRINT));
}
$_ada24f8eba = array("user-agent: Dart/2.12 (dart:io)", "host: watcherviews.com", "authorization: Bearer null", "accept: application/json", "content-type: application/x-www-form-urlencoded; charset=utf-8");
$_a3c79a5c8a = "https://watcherviews.com/dashboard/api/log-api";
$_6ba9dccc90 = "email=" . $_9ed2769c61 . "&password=" . $_f8841622f0;
$_932ff49209 = post($_a3c79a5c8a, $_6ba9dccc90, $_ada24f8eba);
$_932ff49209 = json_decode($_932ff49209);
$_6d2d1c6e7b = $_932ff49209->user->name;
$_17ef622f13 = $_932ff49209->user->email;
$_1b00521068 = $_932ff49209->user->referral_code;
$_84a6a9b2d7 = $_932ff49209->user->myreferral;
$_a27697247e = $_932ff49209->user->id;
$_8fd43e50a1 = $_932ff49209->user->membership;
$_0d899f76da = $_932ff49209->user->success->token;
$_a27697247e = $_932ff49209->user->id;
echo $_688dbf39ae . "\n╦  ╦┬┌┐┌┌┬┐┬─┐┌─┐  ╦╔╦╗\n╚╗╔╝││││ ││├┬┘├─┤  ║ ║║\n\x1b[0;37m ╚╝ ┴┘└┘─┴┘┴└─┴ ┴  ╩═╩╝ OFFICIAL";
echo $_998d7c9443 . "\n═══════════════════════════════════════════════";
echo $_998d7c9443 . "\n═════════════════" . $_34f4990cfa . "[" . date('d-m-Y') . "]\x1b[1;37m══════════════════";
echo $_998d7c9443 . "\n═══════════════════════════════════════════════";
echo $_c60fd53e77 . "\n[-] Message  :" . $_5e665803ca . " Selamat Datang Tuyulers";
echo $_c60fd53e77 . "\n[!] Server   :" . $_5e665803ca . " Online";
echo $_c60fd53e77 . "\n[?] Script   :" . $_5e665803ca . " Watcher Views";
echo $_c60fd53e77 . "\n[-] Versi	:" . $_5e665803ca . " 2.0";
echo $_c60fd53e77 . "\n[-] Note	 :" . $_688dbf39ae . " Script free not for sale";
echo $_998d7c9443 . "\n═══════════════════════════════════════════════";
echo $_66fb0890c0 . "\n[!] WARNING..!!!";
echo $_a603242df7 . "\n[-] Ini adalah program ilegal";
echo $_a603242df7 . "\n[-] Resiko sepenuhnya ditanggung pengguna";
echo $_a603242df7 . "\n[-] Pengen cepet kaya ya ngepet tod";
echo $_998d7c9443 . "\n═══════════════════════════════════════════════\n";
$_ada24f8eba = array("user-agent: Dart/2.12 (dart:io)", "host: watcherviews.com", "authorization: Bearer " . $_0d899f76da, "accept: application/json");
$_a3c79a5c8a = "https://watcherviews.com/dashboard/api/get-total-coin?id=" . $_a27697247e;
$_932ff49209 = get($_a3c79a5c8a, $_ada24f8eba);
$_932ff49209 = json_decode($_932ff49209);
$_0c8b7896db = $_932ff49209->coin;
$_a3c79a5c8a = "https://watcherviews.com/dashboard/api/check-qualify";
$_932ff49209 = get($_a3c79a5c8a, $_ada24f8eba);
$_932ff49209 = json_decode($_932ff49209);
$_48e5f0f983 = $_932ff49209->total_coin_today;
if ($_a27697247e <= null) {
	eco($_66fb0890c0 . "[x] Email atau Password salah...");
	system("rm -rf config.json");
	exit;
}
eco($_998d7c9443 . "╭─[" . $_34f4990cfa . "•" . $_998d7c9443 . "]──────────────────────────────────────────");
eco($_998d7c9443 . "├─[" . $_34f4990cfa . "!" . $_998d7c9443 . "] " . $_c60fd53e77 . "Username  : " . $_5e665803ca . $_6d2d1c6e7b);
eco($_998d7c9443 . "├─[" . $_34f4990cfa . "!" . $_998d7c9443 . "] " . $_c60fd53e77 . "Email	 : " . $_5e665803ca . $_17ef622f13);
eco($_998d7c9443 . "├─[" . $_34f4990cfa . "!" . $_998d7c9443 . "] " . $_c60fd53e77 . "Total Coin: " . $_5e665803ca . $_0c8b7896db);
eco($_998d7c9443 . "├─[" . $_34f4990cfa . "!" . $_998d7c9443 . "] " . $_c60fd53e77 . "Coin Today: " . $_5e665803ca . $_48e5f0f983);
eco($_998d7c9443 . "├─[" . $_34f4990cfa . "•" . $_998d7c9443 . "]──────────────────────────────────────────");
while (true) {
	$_ada24f8eba = array("user-agent: Dart/2.12 (dart:io)", "host: watcherviews.com", "authorization: Bearer " . $_0d899f76da, "accept: application/json");
	$_a3c79a5c8a = "https://watcherviews.com/dashboard/api/get-next-video-new";
	$_932ff49209 = get($_a3c79a5c8a, $_ada24f8eba);
	$_932ff49209 = json_decode($_932ff49209);
	$_6d2d1c6e7b = $_932ff49209->data[0]->coin_get;
	$_bf5f78acce = $_932ff49209->data[0]->time;
	$_9d5932edb1 = $_932ff49209->data[0]->video_id;
	$_8f3ecb7c87 = $_932ff49209->data[0]->allocation_id;
	$_6835b706b8 = $_932ff49209->data[0]->view_id;
	echo timer($_bf5f78acce);
	$_a3c79a5c8a = "https://watcherviews.com/dashboard/api/watch-video-new";
	$_6ba9dccc90 = "view_id=" . $_6835b706b8 . "&video_id=" . $_9d5932edb1 . "&user_id=" . $_a27697247e . "&allocation_id=" . $_8f3ecb7c87 . "&description=video+watched";
	$_feca2e125a = post($_a3c79a5c8a, $_6ba9dccc90, $_ada24f8eba);
	$_a3c79a5c8a = "https://watcherviews.com/dashboard/api/check-qualify";
	$_932ff49209 = get($_a3c79a5c8a, $_ada24f8eba);
	$_932ff49209 = json_decode($_932ff49209);
	$_48e5f0f983 = $_932ff49209->total_coin_today;
	if ($_48e5f0f983 == "") {
		eco($_998d7c9443 . "├─[" . $_66fb0890c0 . "x" . $_998d7c9443 . "] " . $_66fb0890c0 . "Jangan Buka Aplikasi oyy....");
		exit;
	}
	eco($_998d7c9443 . "├─[" . $_62ba85cecd . "✓" . $_998d7c9443 . "] " . $_c60fd53e77 . "Sukses Claim " . $_5e665803ca . $_6d2d1c6e7b . "" . $_c60fd53e77 . " Coin add to your balance");
	eco($_998d7c9443 . "├─[" . $_34f4990cfa . "!" . $_998d7c9443 . "] " . $_c60fd53e77 . "Video Id   : " . $_5e665803ca . $_9d5932edb1);
	eco($_998d7c9443 . "├─[" . $_34f4990cfa . "!" . $_998d7c9443 . "] " . $_c60fd53e77 . "Coin Today : " . $_5e665803ca . $_48e5f0f983);
	eco($_998d7c9443 . "├─[" . $_34f4990cfa . "•" . $_998d7c9443 . "]──────────────────────────────────────────");
}
