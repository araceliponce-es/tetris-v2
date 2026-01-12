/*
 * Copyright (C) 2025 Antonio de Andrés Lema
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
package tetris;

import java.awt.Color;
import java.util.Random;

/**
 * Clase que implementa a peza cadrada do xogo do Tetris
 *
 * @author Profe de Programación
 */
public class Piece {

    /**
     * Referenza ao obxecto xogo
     */
    private Game game;

    /**
     * Referenzas aos catro cadrados que forman a peza
     */
    private Square[] squares = new Square[4];

    /**
     * Construtor da clase, que crea os catro cadrados que forman a peza
     *
     * @param game Referenza á partida actual
     */
    public Piece(Game game) {
        this.game = game;
        
        Color[] colorsToUse = {Color.MAGENTA, Color.ORANGE, Color.BLUE, Color.PINK, Color.CYAN};
        int randIndex= new Random().nextInt(colorsToUse.length);
        
        squares[0] = new Square(Game.MAX_X / 2 - Game.SQUARE_SIDE, 0, colorsToUse[randIndex], game);
        squares[1] = new Square(Game.MAX_X / 2, 0, colorsToUse[randIndex], game);
        squares[2] = new Square(Game.MAX_X / 2 - Game.SQUARE_SIDE, Game.SQUARE_SIDE, colorsToUse[randIndex], game);
        squares[3] = new Square(Game.MAX_X / 2, Game.SQUARE_SIDE, colorsToUse[randIndex], game);
    }

    public Game getGame() {
        return game;
    }

    public void setGame(Game game) {
        this.game = game;
    }

    public Square[] getSquares() {
        return squares;
    }

    public void setSquares(Square[] squares) {
        this.squares = squares;
    }

    /**
     * Move a ficha á dereita se é posible
     *
     * @return true se o movemento da ficha é posible, se non false
     */
    public boolean moveRight() {

        boolean canMove = false;
        
        // x sera igual al valor mas grande de los 4 squares
        int x = Integer.MIN_VALUE;
        for (int i = 0; i < squares.length; i++) {
            if (squares[i].getX() > x) {
                x = squares[i].getX();
            }
        }

   
        int counterValids = 0;

        for (int i = 0; i < squares.length; i++) {
            //es valido?
            if (game.isValidPosition(x + game.SQUARE_SIDE, squares[i].getY())) {
                //se mueve   

                counterValids++;

            }
        }

        if (counterValids == squares.length) {
            for (int j = 0; j < squares.length; j++) {
                squares[j].setX(squares[j].getX() + game.SQUARE_SIDE);

            }
        }

        return canMove;
    }

    /**
     * Move a ficha á esquerda se é posible
     *
     * @return true se o movemento da ficha é posible, se non false
     */
    public boolean moveLeft() {
        boolean canMove = false;

        // x sera igual al valor mas pequeño de los 4 squares
        int x = Integer.MAX_VALUE;
        for (int i = 0; i < squares.length; i++) {
            if (squares[i].getX() < x) {
                x = squares[i].getX();
            }
        }
        
       int counterValids = 0;

        for (int i = 0; i < squares.length; i++) {
            //es valido?
            if (game.isValidPosition(x - game.SQUARE_SIDE, squares[i].getY())) {
                //se mueve   

                counterValids++;

            }
        }

        if (counterValids == squares.length) {
            for (int j = 0; j < squares.length; j++) {
                squares[j].setX(squares[j].getX() - game.SQUARE_SIDE);

            }
        }

        return canMove;
    }

    /**
     * Move a ficha a abaixo se é posible
     *
     * @return true se o movemento da ficha é posible, se non false
     */
    public boolean moveDown() {

        boolean canMove = false;
        // y sera igual al valor mas grande de los 4 squares
        int y = Integer.MIN_VALUE;
        //recorre el array y encuentra el y mas grande
        for (int i = 0; i < squares.length; i++) {
            if (squares[i].getY() > y) {
                y = squares[i].getY();
            }
        }

        //solo .moveDown() necesita que todos los cuadrados sean validos. usa un counter
        int counterValids = 0;
        // revisa cada square
        for (int i = 0; i < squares.length; i++) {
            //es valido?
            if (game.isValidPosition(squares[i].getX(), y + game.SQUARE_SIDE)) {

                counterValids++;
            }
        }

        if (counterValids == squares.length) {
            canMove = true;
            for (int j = 0; j < squares.length; j++) {
                squares[j].setY(squares[j].getY() + game.SQUARE_SIDE);
            }
        }
        return canMove;
    }

    /**
     * Rota a ficha se é posible
     *
     * @return true se o movemento da ficha é posible, se non false
     */
    public boolean rotate() {
        // A rotación da ficha cadrada non supón ningunha variación na ficha,
        // por iso simplemente devolvemos true
        return true;
    }

}
