#!/usr/bin/env python3
"""Generates the static Auris PEQ site (privacy + support, six languages).

Run `python3 build.py` after editing the text below; commit the generated
folders too, GitHub Pages serves them as they are.
"""
import html
import pathlib

CONTACT = "giottinodev@protonmail.me"
UPDATED = {"en": "6 October 2026", "it": "6 ottobre 2026", "de": "6. Oktober 2026",
           "fr": "6 octobre 2026", "es": "6 de octubre de 2026", "ja": "2026年10月6日"}
LANGS = {"en": "English", "it": "Italiano", "de": "Deutsch", "fr": "Français",
         "es": "Español", "ja": "日本語"}

T = {
"en": {
  "privacy": "Privacy Policy", "support": "Support", "updated": "Last updated",
  "privacy_intro": "Auris PEQ is a system-wide parametric equalizer for iPhone and iPad. This policy explains what the app does with your data. Short version: it collects nothing.",
  "privacy_sections": [
    ("What we collect", "Nothing. Auris PEQ has no account, no analytics, no advertising, no crash reporting and no third-party SDKs. The developer runs no server and never receives any information about you or your device."),
    ("Audio", "The sound you play is equalized on your device and sent to your headphones or speaker. It is never recorded, stored or sent anywhere. The microphone permission is requested only because iOS needs a play-and-record audio session to route the sound back to your output; the app does not listen to the microphone. The link between the system extension and the app runs entirely inside your device (127.0.0.1)."),
    ("Settings and presets", "Your equalizer settings and presets are stored on your device. You can optionally turn on iCloud sync in Settings (off by default): presets are then kept in Apple's iCloud key-value storage under your own Apple Account. The developer cannot read them; Apple's privacy policy applies to that storage. Turning the option off stops syncing."),
    ("Tips", "The optional tips are In-App Purchases handled entirely by Apple. The developer receives no names, payment details or other personal information, only the aggregate sales reports Apple provides."),
    ("Children", "The app collects no data from anyone, including children."),
    ("Changes", "If this policy changes, the new version will be published on this page with an updated date."),
    ("Contact", f"Questions about privacy: {CONTACT}"),
  ],
  "support_intro": "Auris PEQ adds a parametric equalizer to every sound on your iPhone or iPad, by showing up as an audio output in Control Center. Requires iOS 27 or later.",
  "support_sections": [
    ("Getting started", "Open the app once, then open Control Center, long-press the audio card and choose “Auris PEQ” as the output. Everything you play now goes through the equalizer and comes out of the headphones or speaker you were using. Choose your previous output again in Control Center to stop."),
    ("I hear no sound", "Open the app and check that it is running (it must stay available in the background), then pick Auris PEQ again in Control Center. If you used “Power off” in the app, reopen the app first."),
    ("The sound stutters for a few seconds", "A short settling time right after choosing Auris PEQ is known; opening heavy apps such as Camera can also cause a brief glitch. If it persists, tell us your device, iOS version and output (see Contact)."),
    ("Bypass", "Use the Bypass switch in the app, or the Auris PEQ control in Control Center, to compare the sound with and without the equalizer."),
    ("iCloud sync", "In Settings you can sync presets through your iCloud account. It is off by default and can be turned off at any time."),
    ("Tips", "The app is free to use. Tips are optional and handled by the App Store; use Restore/Manage Subscriptions in your Apple Account for purchase questions."),
    ("Contact", f"Write to {CONTACT}. Please include your device model, iOS version, the output you use (AirPods, speaker…) and what happened. We read every message."),
  ],
  "home": "Privacy Policy and Support",
},
"it": {
  "privacy": "Informativa sulla privacy", "support": "Supporto", "updated": "Ultimo aggiornamento",
  "privacy_intro": "Auris PEQ è un equalizzatore parametrico di sistema per iPhone e iPad. Questa informativa spiega cosa fa l'app con i tuoi dati. In breve: non raccoglie nulla.",
  "privacy_sections": [
    ("Cosa raccogliamo", "Niente. Auris PEQ non ha account, analytics, pubblicità, segnalazione dei crash né SDK di terze parti. Lo sviluppatore non gestisce alcun server e non riceve mai informazioni su di te o sul tuo dispositivo."),
    ("Audio", "Il suono che riproduci viene equalizzato sul tuo dispositivo e inviato a cuffie o altoparlante. Non viene mai registrato, salvato o inviato altrove. Il permesso del microfono è richiesto solo perché iOS ha bisogno di una sessione audio play-and-record per riportare il suono sulla tua uscita; l'app non ascolta il microfono. Il collegamento tra l'estensione di sistema e l'app avviene interamente dentro il dispositivo (127.0.0.1)."),
    ("Impostazioni e preset", "Le impostazioni dell'equalizzatore e i preset sono salvati sul tuo dispositivo. Puoi attivare facoltativamente la sincronizzazione iCloud in Impostazioni (disattivata di default): i preset sono allora conservati nell'archivio chiave-valore di iCloud, sotto il tuo Apple Account. Lo sviluppatore non può leggerli; per quell'archivio vale l'informativa sulla privacy di Apple. Disattivando l'opzione la sincronizzazione si ferma."),
    ("Mance", "Le mance facoltative sono acquisti in-app gestiti interamente da Apple. Lo sviluppatore non riceve nomi, dati di pagamento o altre informazioni personali, solo i report di vendita aggregati forniti da Apple."),
    ("Minori", "L'app non raccoglie dati da nessuno, minori compresi."),
    ("Modifiche", "Se questa informativa cambia, la nuova versione sarà pubblicata in questa pagina con la data aggiornata."),
    ("Contatti", f"Domande sulla privacy: {CONTACT}"),
  ],
  "support_intro": "Auris PEQ aggiunge un equalizzatore parametrico a ogni suono del tuo iPhone o iPad, comparendo come uscita audio nel Centro di Controllo. Richiede iOS 27 o successivo.",
  "support_sections": [
    ("Per iniziare", "Apri l'app una volta, poi apri il Centro di Controllo, tieni premuta la scheda audio e scegli «Auris PEQ» come uscita. Tutto ciò che riproduci passa dall'equalizzatore ed esce da cuffie o altoparlante che stavi usando. Per smettere, scegli di nuovo la tua uscita precedente nel Centro di Controllo."),
    ("Non sento nulla", "Apri l'app e controlla che sia attiva (deve restare disponibile in background), poi scegli di nuovo Auris PEQ nel Centro di Controllo. Se hai usato «Spegni» nell'app, riaprila prima."),
    ("L'audio scatta per qualche secondo", "Un breve assestamento subito dopo aver scelto Auris PEQ è un comportamento noto; anche aprire app pesanti come Fotocamera può causare un'interruzione breve. Se persiste, scrivici modello, versione di iOS e uscita usata (vedi Contatti)."),
    ("Bypass", "Usa l'interruttore Bypass nell'app, o il controllo Auris PEQ nel Centro di Controllo, per confrontare il suono con e senza equalizzatore."),
    ("Sincronizzazione iCloud", "In Impostazioni puoi sincronizzare i preset tramite il tuo account iCloud. È disattivata di default e puoi spegnerla in qualsiasi momento."),
    ("Mance", "L'app si usa gratis. Le mance sono facoltative e gestite dall'App Store; per domande sugli acquisti usa il tuo Apple Account."),
    ("Contatti", f"Scrivi a {CONTACT}. Indica modello di dispositivo, versione di iOS, uscita usata (AirPods, altoparlante…) e cosa è successo. Leggiamo ogni messaggio."),
  ],
  "home": "Informativa sulla privacy e supporto",
},
"de": {
  "privacy": "Datenschutzerklärung", "support": "Support", "updated": "Zuletzt aktualisiert",
  "privacy_intro": "Auris PEQ ist ein systemweiter parametrischer Equalizer für iPhone und iPad. Diese Erklärung beschreibt, was die App mit deinen Daten macht. Kurz gesagt: Sie erhebt nichts.",
  "privacy_sections": [
    ("Was wir erheben", "Nichts. Auris PEQ hat kein Konto, keine Analyse, keine Werbung, keine Absturzberichte und keine SDKs von Drittanbietern. Der Entwickler betreibt keinen Server und erhält nie Informationen über dich oder dein Gerät."),
    ("Audio", "Der Ton, den du abspielst, wird auf deinem Gerät entzerrt und an Kopfhörer oder Lautsprecher gesendet. Er wird nie aufgenommen, gespeichert oder irgendwohin gesendet. Die Mikrofonberechtigung wird nur verlangt, weil iOS eine Wiedergabe-und-Aufnahme-Audiositzung braucht, um den Ton auf deinen Ausgang zurückzuleiten; die App hört das Mikrofon nicht ab. Die Verbindung zwischen der Systemerweiterung und der App läuft vollständig innerhalb deines Geräts (127.0.0.1)."),
    ("Einstellungen und Presets", "Deine Equalizer-Einstellungen und Presets werden auf deinem Gerät gespeichert. Optional kannst du in den Einstellungen die iCloud-Synchronisierung aktivieren (standardmäßig aus): Die Presets liegen dann im Schlüssel-Wert-Speicher von iCloud unter deiner eigenen Apple-ID. Der Entwickler kann sie nicht lesen; für diesen Speicher gilt die Datenschutzerklärung von Apple. Wenn du die Option ausschaltest, endet die Synchronisierung."),
    ("Trinkgelder", "Die optionalen Trinkgelder sind In-App-Käufe, die vollständig von Apple abgewickelt werden. Der Entwickler erhält keine Namen, Zahlungsdaten oder sonstigen personenbezogenen Daten, nur die zusammengefassten Verkaufsberichte von Apple."),
    ("Kinder", "Die App erhebt von niemandem Daten, auch nicht von Kindern."),
    ("Änderungen", "Ändert sich diese Erklärung, wird die neue Fassung mit aktualisiertem Datum auf dieser Seite veröffentlicht."),
    ("Kontakt", f"Fragen zum Datenschutz: {CONTACT}"),
  ],
  "support_intro": "Auris PEQ fügt jedem Ton auf deinem iPhone oder iPad einen parametrischen Equalizer hinzu, indem es im Kontrollzentrum als Audioausgang erscheint. Erfordert iOS 27 oder neuer.",
  "support_sections": [
    ("Erste Schritte", "Öffne die App einmal, öffne dann das Kontrollzentrum, halte die Audiokarte gedrückt und wähle „Auris PEQ“ als Ausgang. Alles, was du abspielst, läuft nun durch den Equalizer und kommt aus den Kopfhörern oder dem Lautsprecher, die du zuvor genutzt hast. Zum Beenden wählst du im Kontrollzentrum wieder deinen bisherigen Ausgang."),
    ("Ich höre nichts", "Öffne die App und prüfe, ob sie läuft (sie muss im Hintergrund verfügbar bleiben), und wähle dann Auris PEQ im Kontrollzentrum erneut. Falls du in der App „Ausschalten“ benutzt hast, öffne sie zuerst wieder."),
    ("Der Ton ruckelt einige Sekunden", "Eine kurze Einschwingzeit direkt nach der Wahl von Auris PEQ ist bekannt; auch das Öffnen aufwendiger Apps wie Kamera kann kurz stören. Hält es an, schreib uns Gerät, iOS-Version und Ausgang (siehe Kontakt)."),
    ("Bypass", "Mit dem Bypass-Schalter in der App oder dem Auris-PEQ-Steuerelement im Kontrollzentrum vergleichst du den Klang mit und ohne Equalizer."),
    ("iCloud-Synchronisierung", "In den Einstellungen kannst du Presets über deinen iCloud-Account synchronisieren. Sie ist standardmäßig aus und jederzeit abschaltbar."),
    ("Trinkgelder", "Die App ist kostenlos nutzbar. Trinkgelder sind optional und werden vom App Store abgewickelt; bei Fragen zu Käufen nutze deine Apple-ID."),
    ("Kontakt", f"Schreib an {CONTACT}. Bitte nenne Gerätemodell, iOS-Version, den genutzten Ausgang (AirPods, Lautsprecher …) und was passiert ist. Wir lesen jede Nachricht."),
  ],
  "home": "Datenschutz und Support",
},
"fr": {
  "privacy": "Politique de confidentialité", "support": "Assistance", "updated": "Dernière mise à jour",
  "privacy_intro": "Auris PEQ est un égaliseur paramétrique système pour iPhone et iPad. Cette politique explique ce que l'app fait de vos données. En bref : elle ne collecte rien.",
  "privacy_sections": [
    ("Ce que nous collectons", "Rien. Auris PEQ n'a ni compte, ni analyse d'audience, ni publicité, ni rapport de plantage, ni SDK tiers. Le développeur n'exploite aucun serveur et ne reçoit jamais d'information sur vous ou votre appareil."),
    ("Audio", "Le son que vous lisez est égalisé sur votre appareil puis envoyé à vos écouteurs ou à votre haut-parleur. Il n'est jamais enregistré, stocké ni envoyé ailleurs. L'autorisation du micro est demandée uniquement parce qu'iOS exige une session audio lecture-et-enregistrement pour renvoyer le son vers votre sortie ; l'app n'écoute pas le micro. Le lien entre l'extension système et l'app reste entièrement à l'intérieur de l'appareil (127.0.0.1)."),
    ("Réglages et préréglages", "Vos réglages d'égaliseur et vos préréglages sont stockés sur votre appareil. Vous pouvez activer en option la synchronisation iCloud dans les Réglages (désactivée par défaut) : les préréglages sont alors conservés dans le stockage clé-valeur d'iCloud, sous votre propre compte Apple. Le développeur ne peut pas les lire ; la politique de confidentialité d'Apple s'applique à ce stockage. Désactiver l'option arrête la synchronisation."),
    ("Pourboires", "Les pourboires facultatifs sont des achats intégrés gérés entièrement par Apple. Le développeur ne reçoit ni nom, ni coordonnées de paiement, ni autre donnée personnelle, seulement les rapports de ventes agrégés fournis par Apple."),
    ("Enfants", "L'app ne collecte de données auprès de personne, enfants compris."),
    ("Modifications", "Si cette politique change, la nouvelle version sera publiée sur cette page avec une date mise à jour."),
    ("Contact", f"Questions sur la confidentialité : {CONTACT}"),
  ],
  "support_intro": "Auris PEQ ajoute un égaliseur paramétrique à tous les sons de votre iPhone ou iPad en apparaissant comme sortie audio dans le Centre de contrôle. Nécessite iOS 27 ou version ultérieure.",
  "support_sections": [
    ("Pour commencer", "Ouvrez l'app une fois, puis le Centre de contrôle, maintenez la carte audio et choisissez « Auris PEQ » comme sortie. Tout ce que vous lisez passe alors par l'égaliseur et sort sur les écouteurs ou le haut-parleur que vous utilisiez. Pour arrêter, rechoisissez votre sortie précédente dans le Centre de contrôle."),
    ("Je n'entends rien", "Ouvrez l'app et vérifiez qu'elle fonctionne (elle doit rester disponible en arrière-plan), puis rechoisissez Auris PEQ dans le Centre de contrôle. Si vous avez utilisé « Éteindre » dans l'app, rouvrez-la d'abord."),
    ("Le son saccade pendant quelques secondes", "Un court temps d'établissement juste après le choix d'Auris PEQ est connu ; ouvrir des apps lourdes comme Appareil photo peut aussi provoquer une brève coupure. Si cela persiste, indiquez-nous votre appareil, la version d'iOS et la sortie (voir Contact)."),
    ("Bypass", "Utilisez l'interrupteur Bypass dans l'app, ou le contrôle Auris PEQ dans le Centre de contrôle, pour comparer le son avec et sans égaliseur."),
    ("Synchronisation iCloud", "Dans les Réglages, vous pouvez synchroniser les préréglages via votre compte iCloud. Elle est désactivée par défaut et peut être coupée à tout moment."),
    ("Pourboires", "L'app est gratuite. Les pourboires sont facultatifs et gérés par l'App Store ; pour toute question sur un achat, utilisez votre compte Apple."),
    ("Contact", f"Écrivez à {CONTACT}. Indiquez le modèle de votre appareil, la version d'iOS, la sortie utilisée (AirPods, haut-parleur…) et ce qui s'est passé. Nous lisons chaque message."),
  ],
  "home": "Confidentialité et assistance",
},
"es": {
  "privacy": "Política de privacidad", "support": "Soporte", "updated": "Última actualización",
  "privacy_intro": "Auris PEQ es un ecualizador paramétrico de sistema para iPhone y iPad. Esta política explica qué hace la app con tus datos. En resumen: no recopila nada.",
  "privacy_sections": [
    ("Qué recopilamos", "Nada. Auris PEQ no tiene cuenta, analíticas, publicidad, informes de fallos ni SDK de terceros. El desarrollador no gestiona ningún servidor y nunca recibe información sobre ti ni sobre tu dispositivo."),
    ("Audio", "El sonido que reproduces se ecualiza en tu dispositivo y se envía a tus auriculares o altavoz. Nunca se graba, almacena ni envía a ningún sitio. El permiso del micrófono se pide solo porque iOS necesita una sesión de audio de reproducción y grabación para devolver el sonido a tu salida; la app no escucha el micrófono. El enlace entre la extensión del sistema y la app ocurre por completo dentro del dispositivo (127.0.0.1)."),
    ("Ajustes y presets", "Tus ajustes del ecualizador y tus presets se guardan en tu dispositivo. Opcionalmente puedes activar la sincronización con iCloud en Ajustes (desactivada por defecto): los presets se guardan entonces en el almacenamiento clave-valor de iCloud, bajo tu propia cuenta de Apple. El desarrollador no puede leerlos; a ese almacenamiento se aplica la política de privacidad de Apple. Al desactivar la opción se detiene la sincronización."),
    ("Propinas", "Las propinas opcionales son compras dentro de la app gestionadas por completo por Apple. El desarrollador no recibe nombres, datos de pago ni otra información personal, solo los informes de ventas agregados que proporciona Apple."),
    ("Menores", "La app no recopila datos de nadie, tampoco de menores."),
    ("Cambios", "Si esta política cambia, la nueva versión se publicará en esta página con la fecha actualizada."),
    ("Contacto", f"Preguntas sobre privacidad: {CONTACT}"),
  ],
  "support_intro": "Auris PEQ añade un ecualizador paramétrico a todo el sonido de tu iPhone o iPad apareciendo como salida de audio en el Centro de control. Requiere iOS 27 o posterior.",
  "support_sections": [
    ("Primeros pasos", "Abre la app una vez, luego abre el Centro de control, mantén pulsada la tarjeta de audio y elige «Auris PEQ» como salida. Todo lo que reproduzcas pasará por el ecualizador y saldrá por los auriculares o el altavoz que usabas. Para dejar de usarlo, vuelve a elegir tu salida anterior en el Centro de control."),
    ("No oigo nada", "Abre la app y comprueba que está activa (debe seguir disponible en segundo plano); después vuelve a elegir Auris PEQ en el Centro de control. Si usaste «Apagar» en la app, ábrela primero otra vez."),
    ("El sonido se entrecorta unos segundos", "Un breve tiempo de ajuste justo después de elegir Auris PEQ es algo conocido; abrir apps pesadas como Cámara también puede causar un corte breve. Si persiste, cuéntanos tu dispositivo, la versión de iOS y la salida (ver Contacto)."),
    ("Bypass", "Usa el interruptor Bypass de la app, o el control Auris PEQ del Centro de control, para comparar el sonido con y sin ecualizador."),
    ("Sincronización con iCloud", "En Ajustes puedes sincronizar los presets con tu cuenta de iCloud. Está desactivada por defecto y se puede apagar en cualquier momento."),
    ("Propinas", "La app es gratuita. Las propinas son opcionales y las gestiona la App Store; para dudas sobre compras usa tu cuenta de Apple."),
    ("Contacto", f"Escribe a {CONTACT}. Indica el modelo de tu dispositivo, la versión de iOS, la salida que usas (AirPods, altavoz…) y qué ocurrió. Leemos todos los mensajes."),
  ],
  "home": "Privacidad y soporte",
},
"ja": {
  "privacy": "プライバシーポリシー", "support": "サポート", "updated": "最終更新日",
  "privacy_intro": "Auris PEQ は iPhone と iPad 向けのシステム全体に効くパラメトリックイコライザーです。本ポリシーは、アプリがあなたのデータをどのように扱うかを説明します。要点：何も収集しません。",
  "privacy_sections": [
    ("収集する情報", "何もありません。Auris PEQ にはアカウント、解析、広告、クラッシュレポート、サードパーティ製 SDK がありません。開発者はサーバーを運用しておらず、あなたやお使いのデバイスに関する情報を受け取ることもありません。"),
    ("オーディオ", "再生した音はデバイス上でイコライズされ、イヤホンやスピーカーに送られます。録音・保存・外部送信は一切行いません。マイクの許可を求めるのは、音を出力先へ戻すために iOS が再生と録音のオーディオセッションを必要とするためで、アプリがマイクの音を聞くことはありません。システム拡張機能とアプリの間の接続は、すべてデバイス内（127.0.0.1）で完結します。"),
    ("設定とプリセット", "イコライザーの設定とプリセットはデバイスに保存されます。「設定」で iCloud 同期を任意でオンにできます（初期状態はオフ）。オンにすると、プリセットはあなた自身の Apple アカウントの iCloud キー・バリュー・ストレージに保存されます。開発者はそれを読むことができず、このストレージには Apple のプライバシーポリシーが適用されます。オフにすると同期は停止します。"),
    ("チップ", "任意のチップは Apple が完全に処理するアプリ内課金です。開発者は氏名、支払い情報、その他の個人情報を受け取らず、Apple が提供する集計済みの売上レポートのみを受け取ります。"),
    ("お子さま", "本アプリはお子さまを含め、誰からもデータを収集しません。"),
    ("変更", "本ポリシーを変更する場合は、更新日を付けてこのページに新しい版を公開します。"),
    ("お問い合わせ", f"プライバシーに関するご質問：{CONTACT}"),
  ],
  "support_intro": "Auris PEQ はコントロールセンターにオーディオ出力として表示され、iPhone や iPad のすべての音にパラメトリックイコライザーを追加します。iOS 27 以降が必要です。",
  "support_sections": [
    ("はじめに", "アプリを一度開き、コントロールセンターでオーディオのカードを長押しして、出力先に「Auris PEQ」を選びます。再生するすべての音がイコライザーを通り、それまで使っていたイヤホンやスピーカーから出力されます。やめるときは、コントロールセンターで元の出力先を選び直してください。"),
    ("音が出ない", "アプリを開いて動作していること（バックグラウンドで利用可能な状態）を確認し、コントロールセンターで Auris PEQ を選び直してください。アプリで「電源オフ」を使った場合は、先にアプリを開き直してください。"),
    ("数秒間、音がとぎれる", "Auris PEQ を選んだ直後に短い安定時間があることは既知の動作です。カメラのような負荷の高いアプリを開くと、一瞬とぎれることもあります。続く場合は、機種、iOS のバージョン、出力先をお知らせください（お問い合わせ参照）。"),
    ("バイパス", "アプリ内のバイパススイッチ、またはコントロールセンターの Auris PEQ コントロールで、イコライザーあり・なしの音を比較できます。"),
    ("iCloud 同期", "「設定」でプリセットを iCloud アカウント経由で同期できます。初期状態ではオフで、いつでもオフにできます。"),
    ("チップ", "アプリは無料でお使いいただけます。チップは任意で、App Store が処理します。購入に関するご質問は Apple アカウントからお問い合わせください。"),
    ("お問い合わせ", f"{CONTACT} までご連絡ください。機種、iOS のバージョン、使用中の出力先（AirPods、スピーカーなど）、起きたことを添えてください。すべてのメッセージに目を通します。"),
  ],
  "home": "プライバシーポリシーとサポート",
},
}

CSS = """:root{color-scheme:light dark;--bg:#fff;--fg:#1d1d1f;--mut:#6e6e73;--line:#d2d2d7;--acc:#0a66d6}
@media(prefers-color-scheme:dark){:root{--bg:#000;--fg:#f5f5f7;--mut:#a1a1a6;--line:#38383a;--acc:#4da3ff}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:17px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}
main{max-width:42rem;margin:0 auto;padding:2rem 1rem 4rem}
h1{font-size:2rem;line-height:1.2;margin:.5rem 0 .25rem}h2{font-size:1.2rem;margin:2rem 0 .4rem}
p{margin:.4rem 0}a{color:var(--acc)}.mut{color:var(--mut);font-size:.9rem}
nav{display:flex;flex-wrap:wrap;gap:.4rem 1rem;padding-bottom:.8rem;border-bottom:1px solid var(--line);font-size:.95rem}
nav .cur{font-weight:600;text-decoration:none;color:var(--fg)}footer{margin-top:3rem;padding-top:1rem;border-top:1px solid var(--line)}
ul.l{list-style:none;padding:0}ul.l li{margin:.6rem 0}"""


def page(lang, kind):
    t = T[lang]
    title = t[kind]
    intro = t[f"{kind}_intro"]
    secs = "".join(f"<h2>{html.escape(h)}</h2><p>{html.escape(p)}</p>" for h, p in t[f"{kind}_sections"])
    other = "support" if kind == "privacy" else "privacy"
    langs = " ".join(
        f'<a class="cur" href="../{c}/{kind}.html" hreflang="{c}">{n}</a>' if c == lang
        else f'<a href="../{c}/{kind}.html" hreflang="{c}" lang="{c}">{n}</a>'
        for c, n in LANGS.items())
    return f"""<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Auris PEQ – {html.escape(title)}</title>
<link rel="stylesheet" href="../style.css"></head>
<body><main>
<nav>{langs}</nav>
<h1>Auris PEQ – {html.escape(title)}</h1>
<p class="mut">{t['updated']}: {UPDATED[lang]}</p>
<p>{html.escape(intro)}</p>
{secs}
<footer><a href="{other}.html">{html.escape(t[other])}</a></footer>
</main></body></html>
"""


def index():
    items = "".join(f'<li><a href="{c}/privacy.html" lang="{c}">{n}</a> · '
                    f'<a href="{c}/support.html" lang="{c}">{html.escape(T[c]["support"])}</a>'
                    f' · <span class="mut">{html.escape(T[c]["privacy"])}</span></li>' for c, n in LANGS.items())
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Auris PEQ</title><link rel="stylesheet" href="style.css"></head>
<body><main><h1>Auris PEQ</h1><p class="mut">Privacy Policy · Support</p><ul class="l">{items}</ul></main></body></html>
"""


root = pathlib.Path(__file__).parent
(root / "style.css").write_text(CSS)
(root / "index.html").write_text(index())
(root / ".nojekyll").write_text("")
for lang in LANGS:
    d = root / lang
    d.mkdir(exist_ok=True)
    for kind in ("privacy", "support"):
        (d / f"{kind}.html").write_text(page(lang, kind))
print("ok")
