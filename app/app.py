
import os
import pymysql

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/feedback", methods=["POST"])
def salvar_feedback():
    nome = request.form.get("nome", "").strip()
    email = request.form.get("email", "").strip()
    comentario = request.form.get("comentario", "").strip()

    if not nome or not email or not comentario:
        return "Preencha todos os campos.", 400

    try:
        conexao = pymysql.connect(
            host=os.environ.get("MYSQL_HOST", "mysql"),
            user=os.environ["MYSQL_USER"],
            password=os.environ["MYSQL_PASSWORD"],
            database=os.environ["MYSQL_DATABASE"]
        )

        try:
            with conexao.cursor() as cursor:
                sql = """
                    INSERT INTO comentarios
                    (nome, email, comentario)
                    VALUES (%s, %s, %s)
                """
                cursor.execute(
                    sql, (nome, email, comentario)
                )

            conexao.commit()
        finally:
            conexao.close()

    except (pymysql.MySQLError, KeyError):
        app.logger.exception("Erro ao salvar feedback")
        return "Erro ao salvar o comentário.", 500

    return "Feedback enviado com sucesso!"


@app.route("/health")
def verificar_saude():
    return {"status": "online"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

