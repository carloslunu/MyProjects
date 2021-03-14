package com.carlos.juegoimagenes;

import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.content.Context;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.os.CountDownTimer;
import android.view.MotionEvent;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

import java.util.Random;

public class PantallaJuego extends AppCompatActivity {
    private TextView nombreusuario;
    private TextView puntuacionmaxima;
    private TextView puntuacion;
    private TextView contador;
    private ImageView imagen;
    private Button botonresetear;
    int maxScoreVal = 0;
    int myScore = 0;
    String userName;

    @SuppressLint("ClickableViewAccessibility")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_second);
        nombreusuario = findViewById(R.id.nomjuador);
        puntuacionmaxima = findViewById(R.id.puntuacio);
        puntuacion = findViewById(R.id.puntuaciopartida);
        contador = findViewById(R.id.contador);
        imagen = findViewById(R.id.Imagenjuego);
        botonresetear = findViewById(R.id.botonreiniciar);


        imagen.setOnTouchListener(new View.OnTouchListener() {
            @Override
            public boolean onTouch(View v, MotionEvent event) {
                if (event.getAction() == MotionEvent.ACTION_UP) {
                    float x = v.getX();
                    float y = v.getY();
                    Random r = new Random();
                    int random_x = r.nextInt((int) x - 100) + 300;
                    int random_y = r.nextInt((int) y - 100) + 300;
                    imagen.setX(random_x);
                    imagen.setY(random_y);
                    myScore++;
                    puntuacion.setText(String.valueOf(myScore));

                    return true;
                }
                return false;
            }
        });
        Bundle b = getIntent().getExtras();
        if (b != null) {
            userName = b.getString("NOMBRE");
            nombreusuario.setText(userName);
              mirarpuntuacionmáxima();
              contadorjuego();
        }
    }

    private void mirarpuntuacionmáxima() {

        SharedPreferences sp2 = getSharedPreferences("puntuaciones", Context.MODE_PRIVATE);
        if (sp2 != null) {
            maxScoreVal = sp2.getInt("max_score", 0);
        }
        puntuacionmaxima.setText(String.valueOf(maxScoreVal));
        puntuacionmaxima.setTextSize(35);
    }

    private void guardarRecord() {
        SharedPreferences sp = getSharedPreferences("puntuaciones", Context.MODE_PRIVATE);
        SharedPreferences.Editor editor = sp.edit();
        editor.putInt("max_score", myScore);
        editor.putString("nombre", userName);
        editor.apply();
        editor.clear();
    }

    private void contadorjuego() {
        new CountDownTimer(20000, 1000) {
            public void onTick(long millisUntilFinished) {
                contador.setText(String.valueOf(millisUntilFinished / 1000));
            }

            public void onFinish() {
                if (myScore > maxScoreVal) {
                    contador.setText("Ha terminat el joc,felicitats,has superat el record del joc");
                    guardarRecord();
                } else {
                    contador.setText("Ha terminat el joc,la teva puntuació es: " + myScore);
                }
                botonresetear.setEnabled(true);
            }
        }.start();
    }

    public void vueltaatras(View view) {
        finish();
    }

    public void reiniciar(View view) {
        myScore = 0;
       puntuacion.setText(String.valueOf(myScore));
        contadorjuego();
        botonresetear.setEnabled(false);
    }
    //el botón reiniciar aparecerá de un color (azul) durante el juego para indicar que aún no se puede utilizar y cuando termine el contador cambiará al color del otro botón(amarillo) indicando que ya se puede utilizar
}