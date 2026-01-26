/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ahorcado.parte1;

import java.util.Scanner;

/**
 *
 * @author Araceli,Diego,Óscar
 */
public class HiddenWord {

    private char[] characters;
    private boolean[] hits;

    public char[] getCharacters() {
        return characters;
    }

    public void setCharacters(char[] characters) {
        this.characters = characters;
    }

    public boolean[] getHits() {
        return hits;
    }

    public void setHits(boolean[] hits) {
        this.hits = hits;
    }

    public HiddenWord(String palabra) {
        characters = palabra.toCharArray();
        hits = new boolean[characters.length];
        for (int i = 0; i < hits.length; i++) {
            hits[i] = false;
        }
    }

 

    public boolean checkChar(char caracter) {
        boolean charFound = false;
        for (int i = 0; i < characters.length; i++) {
            if (caracter == characters[i]) {
                hits[i] = true;
                charFound = true;
            }
        }
        return charFound;
    }

    public String show() {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < characters.length; i++) {
            if (hits[i]) {
                sb.append(characters[i]);
            } else {
                sb.append("-");
            }
        }
        return sb.toString();
    }

    public String showBis() {

        for (int i = 0; i < characters.length; i++) {
            if (hits[i]) {
                System.out.print(characters[i]);
            } else {
                System.out.print("-");
            }
        }
        return "";
    }

    public String showFullWord() {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < characters.length; i++) {
            sb.append(characters[i]);
        }
        return sb.toString();
    }

    public boolean isVisible() {
        boolean acertada = false;
        for (int i = 0; i < hits.length; i++) {
            if (hits[i] ==false) {
                acertada = false;

            } else {
                acertada = true;
                for (i = 0; i < hits.length; i++) {
                    if (hits[i] ==false) {
                        acertada = false;
                    }
                }
            }
        }
        return acertada;
    }
}
