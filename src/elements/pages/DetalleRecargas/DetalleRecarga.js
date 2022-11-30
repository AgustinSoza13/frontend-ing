import React, { Component } from 'react'
import { Col, Container, Row } from 'reactstrap'
import ListaDetalleRecarga from './ListaDetalleRecarga'
import NuevaDetalleRecargaModal from './NuevoModalDetalleRecarga'

import axios from 'axios'

class DetalleRecarga extends Component {
    state = {
        recargas: []
    }

    componentDidMount() {
        this.resetState()
    }

    getRecargas = () => {
        axios.get('http://127.0.0.1:8000/Inventario_detalles_descarga/').then(res => this.setState({ recargas: res.data }))
    }

    resetState = () => {
        this.getRecargas()
    }

    render() {
        return (
            <Container style={{ marginTop: "20px" }}>
                <a href="javascript:history.back()"> Volver Atrás</a>
                <Row>
                    <Col>
                        <ListaDetalleRecarga recargas={this.state.recargas} resetState={this.resetState}/>
                    </Col>
                </Row>
                <Row>
                    <Col>
                        <NuevaDetalleRecargaModal resetState={this.resetState}/>
                    </Col>
                </Row>
            </Container>
        )
    }
}

export default DetalleRecarga