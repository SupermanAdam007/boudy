﻿<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01">
<html>
  <head>
    <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
    <meta name="keywords" content="boudy, bivaky, útulny" />
    <meta
      name="description"
      content="Otevřená databáze horských chat, bivakovacích boud a bivaků"
    />
    <title>
      Boudy (www.boudy.info) - hlavní informace
    </title>
    <link
      rel="stylesheet"
      href="https://unpkg.com/leaflet@1.0.3/dist/leaflet.css"
    />
    <link rel="stylesheet" type="text/css" href="css/_stranka.css" />
    <link rel="stylesheet" type="text/css" href="css/bouda.css" />
    <script type="text/javascript" src="js/jquery-3.2.0.min.js"></script>
    <script language="JavaScript">
      function menu_Z(ID, color_z) {
        var el = document.getElementById(ID);
        el.style.backgroundColor = color_z;
      }
      function menu_V(ID, color_v) {
        var el = document.getElementById(ID);
        el.style.backgroundColor = color_v;
      }
    </script>
  </head>
  <body>
    <div class="stranka">
      <div class="plocha">
        <div class="titulek">
          <div
            class="titulek_logo"
            style="background-image: url(grafika/obr_titulek/obr_22.png);"
          >
            <div class="titulek_cz_en">
              <a href="bouda.php?txt=cz" class="titulek_cz_en">Česky</a> |
              English
            </div>
            <div class="titulek_popis">
              <div class="titulek_nadpis">
                www.boudy.info
              </div>
              Otevřená databáze horských chat, bivakovacích boud a bivaků
            </div>
            <div class="terminator"></div>
          </div>
        </div>
        <div class="hl_menu">
          <span class="hl_menu">
            <a
              class="hl_menu"
              href="index.php?txt=cz"
              title="Návrat na hlavní stránku..."
            >
              Index
            </a>
          </span>
          <span class="hl_menu">
            <a
              class="hl_menu"
              href="hledat.php?txt=cz"
              title="Hledání objektů podle země / pohoří..."
            >
              Vyhledat objekt
            </a>
          </span>
          <span class="hl_menu">
            <a
              class="hl_menu"
              href="pridat.php?txt=cz"
              title="Přidat nový objekt..."
            >
              Přidat objekt
            </a>
          </span>
          <span class="hl_menu">
            <a
              class="hl_menu"
              href="mapa.php?txt=cz"
              title="Hledání objektů podle mapy..."
            >
              Zobrazit mapu
            </a>
          </span>
          <span class="hl_menu">
            <a
              class="hl_menu"
              href="export.php?txt=cz"
              title="Výběr a export GPS souřadnic objektů..."
            >
              Export GPS
            </a>
          </span>
        </div>
        <div class="nadpis">
          Chyba
        </div>
        <div class="podnadpis">
          Nelze zobrazit požadovanou stránku
        </div>
        <div class="sloupek_P"></div>
        <div class="sloupek_L">
          <div class="chyba">
            <div class="chyba_nadpis">
              Chyba !!!
            </div>
            Chyba v definici parametrů stránky, nebylo specifikováno id
            zobrazovaného objektu...
          </div>
        </div>
        <div class="terminator"></div>
        <div class="konec">
          <b>&copy;</b> www.boudy.info | veškteré informace bez záruky | PHP
          4.4.8 | poslední úprava: 11.04.2012 23:07:35 V.A.
        </div>
      </div>
    </div>
  </body>
</html>
