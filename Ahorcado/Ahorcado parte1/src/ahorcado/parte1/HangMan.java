/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ahorcado.parte1;

import java.util.ArrayList;

/**
 *
 * @author Araceli,Diego,Óscar
 */
public class HangMan {

    public static final int MAX_FAILS = 6;
    private HiddenWord hiddenWord;
    private ArrayList<Character> fails = new ArrayList();

    public HangMan(String palabra) {
        hiddenWord = new HiddenWord(palabra);
    }

    public ArrayList<Character> getFails() {
        return fails;
    }

    public String getStringFails() {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < fails.size(); i++) {
            sb.append(fails.get(i)).append(" ");
        }
        return sb.toString();
    }

    public String showHidenWord() {
        return hiddenWord.show();
    }

    public String showFullWord() {
        return hiddenWord.showFullWord();
    }

    public void tryChar(char caracter) {
        if (!hiddenWord.checkChar(caracter)) {
            fails.add(caracter);
        } 
    }

    public boolean isGameOver() {
        return hiddenWord.isVisible() || maxFailsExceeded();
    }

    public boolean maxFailsExceeded() {
        boolean excedido;
        excedido = fails.size() == MAX_FAILS;
        return excedido;
    }

}
